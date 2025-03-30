from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from rest_framework.response import Response
from .serializers import LikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from notifications.utils import create_notification
from rest_framework import filters, status
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


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all() 
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        create_notification(post.author, request.user, "liked your post", post)
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            like = Like.objects.get(user=request.user, post_id=pk)
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)
