# urls.py
from django.urls import path 
from .views import SubcourseList, SubcourseUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('subcourse/', SubcourseList.as_view(), name= "create-materi-list"),
    path('subcourse/<int:pk>/', SubcourseUpdateDelete.as_view(), name= "materi-details")
]