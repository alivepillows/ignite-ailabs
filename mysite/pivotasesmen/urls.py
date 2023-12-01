# urls.py
from django.urls import path 
from .views import PivotAsesmenListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('pivotasesmen/', PivotAsesmenListView.as_view(), name= "create-asesmen-list"),
    # path('pivotasesmen/<int:pk>/', AsesmenUpdateDeleteView.as_view(), name= "subasesmen-details")
]
