from django.conf.urls import url, include
from blog import views

urlpatterns = [
            url(r'^$', views.index, name="index"),
            url(r'^view/(?P<slug>[^\.]+)/$', views.view_post, name='view_blog_post'),
            url(r'^category/(?P<category>[^\.]+)/$', views.view_category, name='view_blog_category'),
            ]
