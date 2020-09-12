from django.urls import path
from notification.views import NotificationView

urlpatterns = [
    path('notifications/<int:user_id>/', NotificationView.as_view())
]