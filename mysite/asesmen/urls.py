# urls.py
from django.urls import path 
from .views import AsesmenListView, AsesmenUpdateDeleteView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('asesmen/', AsesmenListView.as_view(), name= "create-asesmen-list"),
    path('asesmen/<int:pk>/', AsesmenUpdateDeleteView.as_view(), name= "subasesmen-details")
]