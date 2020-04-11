from django.urls import path
from .views import RegistrationAPIView, UserDetailsAPIView

urlpatterns = [
    path('user', RegistrationAPIView.as_view()),
    path('user/<int:pk>', UserDetailsAPIView.as_view())
]
