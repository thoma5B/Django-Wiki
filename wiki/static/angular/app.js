      var BASE_URL = "http://127.0.0.1:8000/api/v1/"
      var Etherpad_HOST_URL = "http://pad.open-academy.eu"
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
                slug = URLify(article.title)
                return slug == Slug;
              });
              // content = $http.get()
              callback(article);
            })
          },
          post: function(Slug, content, callback){
            var object = {"content": content, "title":title}
            $http({
              method: 'POST',
              data: data,
              url: BASE_URL + "entry/" + Slug,  // ?? or number ?? check in tastypie how to post
            }).success(callback); // TODO: implement cycling button
          }
        }
      })

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
          console.log(article)
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
                articleFactory.post(slug, data, function(){
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

// submit article to database
// var data = JSON.stringify({
//     "body": "blabla bla",
//     "pub_date": "2011-05-22T00:46:38",
//     "slug": "another-post",
//     "title": "Another Post"
// });

// $.ajax({
//   url: 'http://localhost:8000/api/v1/entry/',
//   type: 'POST',
//   contentType: 'application/json',
//   data: data,
//   dataType: 'json',
//   processData: false
// })

