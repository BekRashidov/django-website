from django.urls import path
from . import views
from . import models

#Template tagging
app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(template_name='index.html'), name='index'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

    
]
