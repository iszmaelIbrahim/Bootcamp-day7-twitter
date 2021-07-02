
from django.urls import path

# from . import views
from .views import (
    PostDetailView, 
    FollowersListView, 
    FollowsListView,
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
    
    )
    

urlpatterns = [
    # path('', TweetListView.as_view(), name='home'),
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),


]