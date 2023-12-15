from django.urls import path 
from .views import UserListCreate, UserRetrieveUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user/', UserListCreate.as_view(), name= "create-user-list"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name= "user-details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)