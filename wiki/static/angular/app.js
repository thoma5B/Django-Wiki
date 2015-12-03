// Angular app that 
// - controls full text search and 
// - manages get and post with Django-Api 

"use strict"

var BASE_URL = "http://127.0.0.1:8000/api/v1/"
var Etherpad_HOST_URL = "http://pad.open-academy.eu"

// define mainApp and dependencies
var mainApp = angular.module('mainApp', ['ngRoute','ngSanitize']);

// console.log('djangoUrl', djangoUrl)

mainApp.config(function($routeProvider) {  //TODO: put js in app.js and 
  $routeProvider
    .when('/', {
      templateUrl: 'articlelist.html',
      controller: 'MainController'
    })
    .when('/:articleSlug', {
      templateUrl: 'article_view.html',
      controller: 'EtherpadController'
    })
    .otherwise({
      redirectTo: '/'
    })
})

mainApp.factory('articleFactory', function($http){
  
  function getData(callback){
    $http({
      method: 'GET',
      url: BASE_URL + "content/",
      cache: true
    }).success(callback);
  }

  function getLatestArticles(callback){
    getData(function(data) {
      var articles = data.objects
      getLatest(articles, function(articles){
        callback(articles)
      })
    })
  }

  return {
    list: function(callback) {
      getLatestArticles(callback)
    },
    find: function(Slug, callback){
      getLatestArticles(function(articles) {
        console.log(articles) // undefined
        var article = articles.find( function(article){
          var slug = URLify(article.title)
          return slug == Slug;
        });
        // content = $http.get()
        callback(article);
      })
    },
    post: function(article, callback){
      var now = new Date().format("UtcDateTime");
      // article.modified = now
      var content_date = {content:article.content, modified:now}
      // console.log(data)
      var id = article.id
      $http({
        url: BASE_URL + "content/" + id + "/",  // ?? or number ?? check in tastypie how to post
        method: 'PATCH',
        contentType: 'application/json',
        data: JSON.stringify(content_date),
        dataType: 'json',
        processData: false
      })
      .success(callback) // TODO: implement cycling button
      .error( function(){
        console.log('Doesnt exist yet. Will create new one .. not implemented')
      })
    }
  }
})
// /api/v1/slug -> id; content "article":"/api/v1/article/{{id}}/", id: highest possible id
// -H "Access-Control-Request-Method: POST" -H "Access-Control-Request-Headers: X-Requested-With" -X OPTIONS --verbose
// to obtain the last of the articles of the same title
function getLatest(articles, callback){
  // console.log('articles: ',articles)
  var len = articles.length
  var unique_list = []
  var titles = _(articles).map(function(item){ return item.title })
  _.uniq(titles).forEach( function(title, i){
    var last = _(articles).findLastIndex({'title': title}) 
    unique_list.push(articles[last])
  })
  callback(unique_list)
}

// MainController.$inject = ['$scope', '$http', articleFactory]
mainApp.controller('MainController', MainController)
function MainController ($scope, $http, articleFactory){
  articleFactory.list( function(articles) {
    // console.log('in controller: ',articles)
    addSlugs(articles)
    $scope.articles = articles
  })
}

// EtherpadController.$inject = ['$scope', '$routeParams', '$http']
mainApp.controller('EtherpadController', EtherpadController)
function EtherpadController ($scope, $routeParams, $http, articleFactory){
  articleFactory.find($routeParams.articleSlug, function(article) {
    var slug = URLify(article.title)
    article.slug = slug
    console.log('article in wiki', article)
    var padName = article.title.replace(' ','_') // here: capital letter admitted
    $scope.article = article
    $scope.head = '<div id="remark"> Each article is required to have exactly one heading of type "heading 1" </div>'

    $scope.edit = function(){
      $('#Container').empty()
      $('#Container').pad({
        'padId': padName,
        'host': Etherpad_HOST_URL,
        'showChat':'false'
      })
    }

    $scope.publish = function(){
      $('#Container').empty()
      $('#Container').pad(
        {'padId':padName, 'getContents':'Container'}, 
        function(data){
          console.log('data in pad:', data)
          article.content = data
          articleFactory.post(article, function(){
            console.log(data, 'posted!')
          })
        }
      )
    }

    $scope.edit()
  })
}

function addSlugs(articles){
  _(articles).map( function(article){
    article.slug = URLify(article.title)
    return article
  })
}
// $(document).ready(function(){

// mainApp.directive('pad', function(){
//   return {
//     restrict:'A',
//     link: function(scope,el,atts){
//       console.log('el.slice(2)',el.slice(2))
//       el.pad({'getContents': el.slice(2)})
//     }
//   }
// })


// $.ajax({
//   url: 'http://localhost:8000/api/v1/entry/',
//   type: 'POST',
//   contentType: 'application/json',
//   data: data,
//   dataType: 'json',
//   processData: false
// })

