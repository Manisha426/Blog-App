from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='BlogList'),
    path('write/', views.CreateBlog.as_view(), name='CreateBlog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
]
