from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^success/$', views.success, name='success'),
	url(r'^email/$', views.email, name='email'),
	url(r'^post/$', views.post, name='post'),
	url(r'^pdf/$', views.pdf, name='pdf'),
	url(r'^restapi/$', views.employeelist.as_view()),
]
