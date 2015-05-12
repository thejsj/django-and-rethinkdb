"""django_and_rethinkdb URL Configuration

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
from django_and_rethinkdb.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^auth/', include([
        url(r'^signup/', 'django_and_rethinkdb.views.signup', name='signup'),
        url(r'^login/', 'django_and_rethinkdb.views.login', name='login'),
    ])),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django_and_rethinkdb.views.main', name='main'),
    url(r'^config.js$', 'django_and_rethinkdb.views.config', name='config')
]
