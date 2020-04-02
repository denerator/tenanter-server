from django.urls import path
from . import views

urlpatterns = [
    path('flat/', views.FlatCreationApiView.as_view()),
    path('flat/user/<int:user_id>/', views.FlatsByUser.as_view()),
    path('flat/<int:pk>/', views.FlatDetailsApiView.as_view()),
    path('tenant/', views.TenantSigningAPIView.as_view()),
]
