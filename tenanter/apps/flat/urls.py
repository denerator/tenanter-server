from django.urls import path
from . import views

urlpatterns = [
    path('flat/', views.FlatCreationApiView.as_view()),
    path('flats/<int:user_id>/', views.FlatsByUser.as_view()),
    path('flat/<int:pk>/', views.FlatDetailsApiView.as_view()),
    path('tenant/', views.TenantSigningAPIView.as_view()),
    path('bills/agreement', views.FlatBillsCreationAPIView.as_view()),
    path('flat/bills/agreement/<int:flat>/', views.BillsByFlatAPIView.as_view()),
    path('bill/agreement/<int:pk>/', views.BillsEditAPIView.as_view()),
]
