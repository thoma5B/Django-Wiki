"""learningproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^/', include(app.urls)),
]


from django.conf.urls.i18n import i18n_patterns
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
urlpatterns += [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
# print 'django.conf.urls.i18n::::', url(r'^i18n/', include('django.conf.urls.i18n'))
urlpatterns += i18n_patterns(
    url(r'^notifications/', get_nyt_pattern()),
    url(r'', get_wiki_pattern()),
)
# urlpatterns = i18n_patterns(*urlpatterns)


from tastypie.api import Api
from wiki.api import ArticleResource, ArticleRevisionResource#, UserResource
v1_api = Api(api_name='v1')
# v1_api.register(UserResource())
v1_api.register(ArticleResource())
v1_api.register(ArticleRevisionResource())
urlpatterns += [
    url(r'^api/', include(v1_api.urls)),
]
