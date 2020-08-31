from django.conf.urls import url
from blog import views

#Template tagging
app_name = 'blog'

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    #url(r'', views.PostList.as_view(), name='index'),
    url(r'^list/$', views.PostList.as_view(), name='index'),
    url(r'<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
