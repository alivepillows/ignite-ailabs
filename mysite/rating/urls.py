 # urls.py
from django.urls import path 
from .views import RatingList
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('rating/', RatingList.as_view(), name= "create-ide-list")
]