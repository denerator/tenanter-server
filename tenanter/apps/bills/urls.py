from django.urls import path
from . import views

urlpatterns = [
    path('bills/agreement', views.FlatBillsCreationAPIView.as_view()),
    path('bills/history', views.BillsHistoryCreationAPIView.as_view()),
    path('flat/bills/agreement/<int:flat>/',
         views.BillsByFlatAPIView.as_view()),
    path('flat/bills/history/<int:flat>/',
         views.BillsHistoryByFlatAPIView.as_view()),
    path('bill/agreement/<int:pk>/', views.BillEditAPIView.as_view()),
    path('bill/history', views.BillHistoryAPIView.as_view()),
]
