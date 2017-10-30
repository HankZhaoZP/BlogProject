from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns=[
    # url(r'^$', views.index, name='index'),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.Archives.as_view(), name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$',views.categorys,name='categorys')
    url(r'^category/(?P<pk>[0-9]+)/$',views.Categorys.as_view(),name='categorys'),
    url(r'search/$',views.search,name='search')
]