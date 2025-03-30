from django.urls import path
from .views import NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications-list'),
    path('<int:pk>/read/', MarkNotificationAsReadView.as_view(), name='mark-notification-read'),
]