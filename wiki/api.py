from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from wiki.models import Article, ArticleRevision

from django.contrib.auth.models import User
from tastypie import fields



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        # resource_name = 'user'
        # one of the following two
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']



class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        # resource_name = 'article' # this is the default resource name
        authorization = Authorization()

class ArticleRevisionResource(ModelResource):
    class Meta:
        queryset =  ArticleRevision.objects.all()
        resource_name = 'content'
        fields = ['content','title']
        authorization = Authorization()
