from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from wiki.models import Article, ArticleRevision, URLPath

from django.contrib.auth.models import User
from tastypie import fields


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        # one of the following two
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # excludes = ['email', 'password', 'is_active',
        #               'is_staff', 'is_superuser']
        allowed_methods = ['get']


class ArticleResource(ModelResource):
    current_revision = fields.ToOneField('wiki.api.ArticleRevisionResource', 'current_revision')
    
    class Meta:
        queryset = Article.objects.all()
        # url = get_absolute_url
        resource_name = 'article'  # this is the default resource name
        # fields = ['url']
        filtering = {'current_revision': ALL}
        authorization = Authorization()


class ArticleRevisionResource(ModelResource):
    article = fields.ForeignKey(ArticleResource, 'article')

    class Meta:
        queryset = ArticleRevision.objects.all()
        resource_name = 'content'
        # fields = ['id', 'title', 'modified', 'resource_uri', 'deleted', 'article']
        filtering = {'article': ALL_WITH_RELATIONS}
        authorization = Authorization()


class SlugResource(ModelResource):
    article = fields.ForeignKey(ArticleResource, 'article')
    # obj_get

    class Meta:
        queryset = URLPath.objects.get_queryset()
        resource_name = 'slug'
        # fields = ['slug']
        filtering = {'article': ALL_WITH_RELATIONS}
        authorization = Authorization()
