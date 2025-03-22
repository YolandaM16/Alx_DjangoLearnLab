from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import (
    RegisterView,
    Profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/register/', RegisterView, name="register"),
    path('accounts/login/', LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    path('accounts/profile/', Profile, name="profile"),
    path('posts/', PostListView.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # URL for creating a new comment on a specific post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    
    # URL for updating a comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    # URL for deleting a comment (optional, but recommended)
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]
