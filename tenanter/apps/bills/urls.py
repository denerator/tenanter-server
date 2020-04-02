from django.urls import path
from . import views

urlpatterns = [
    path('bills/agreement', views.FlatBillsCreationAPIView.as_view()),
    path('flat/bills/agreement/<int:flat>/',
         views.BillsByFlatAPIView.as_view()),
    path('bill/agreement/<int:pk>/', views.BillsEditAPIView.as_view()),
]
