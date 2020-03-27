from django.conf.urls import url
from .views import RegistrationAPIView

urlpatterns = [
    url(r'^user/?$', RegistrationAPIView.as_view()),
]
