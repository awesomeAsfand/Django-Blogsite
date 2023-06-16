from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.PostList, name='home'),
    path('detail/<int:pk>/', views.PostDetail, name='detail'),
    path('comment/<int:pk>/', views.Commnet, name='comment'),

]
