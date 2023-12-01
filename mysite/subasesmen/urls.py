# urls.py
from django.urls import path 
from .views import SubAsesmenList, SubAsesmenUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('subasesmen/', SubAsesmenList.as_view(), name= "create-asesmen-list"),
    path('subasesmen/<int:pk>/', SubAsesmenUpdateDelete.as_view(), name= "subasesmen-details")
]