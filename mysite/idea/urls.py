 # urls.py
from django.urls import path 
from .views import IdeList, IdeUpdateRetrieveDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('ide/', IdeList.as_view(), name= "create-ide-list"),
    path('ide/<int:pk>/', IdeUpdateRetrieveDelete.as_view(), name= "ide-details")
]