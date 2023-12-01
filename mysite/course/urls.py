# urls.py
from django.urls import path 
from .views import CourseList, CourseUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('course/', CourseList.as_view(), name= "create-corse-list"),
    path('course/<int:pk>/', CourseUpdateDelete.as_view(), name= "course-details")
]