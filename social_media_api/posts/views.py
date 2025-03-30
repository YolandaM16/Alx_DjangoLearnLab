from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from rest_framework import filters
from .serializers import PostSerializer, CommentSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts.
    Supports CRUD operations with permissions and search filtering.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content'] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.
    Supports CRUD operations with permissions.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  