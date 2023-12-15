# urls.py
from django.urls import path 
from .views import CourseList, CourseUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('course/', CourseList.as_view(), name= "create-corse-list"),
    path('course/<int:pk>/', CourseUpdateDelete.as_view(), name= "course-details")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)