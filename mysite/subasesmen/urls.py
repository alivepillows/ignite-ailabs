from django.urls import path 
from .views import SubAsesmenListCreateView, AsesmenList
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('sub-asesmen/', SubAsesmenListCreateView.as_view(), name='create-sub-asesmen-list' ),
    path('sub-asesmen/<int:pk>/', SubAsesmenListCreateView.as_view(), name='sub-asesmen-detail'),
    path('asesmen/', AsesmenList.as_view(), name="asesmen-list")
]

