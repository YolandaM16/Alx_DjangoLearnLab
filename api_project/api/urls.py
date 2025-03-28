from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list')
]

urlpatterns = [
    path('api/', include(router.urls)),
]