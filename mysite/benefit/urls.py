 # urls.py
from django.urls import path 
from .views import BenefitList,BenefitUpdateRetrieveDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('benefit/', BenefitList.as_view(), name= "create-benefit-list"),
    path('benefit/<int:pk>/', BenefitUpdateRetrieveDelete.as_view(), name= "benefit-details")
]