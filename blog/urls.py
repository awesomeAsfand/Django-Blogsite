from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.PostList, name='home'),
    path('<int:pk>/', views.PostDetail, name='detail'),
    # path('comments/', views.comments, name='add-comment'),

]