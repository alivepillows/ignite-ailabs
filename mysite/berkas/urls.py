from django.urls import path 
from .views import BerkasList, BerkasUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('berkas/', BerkasList.as_view(), name= "create-berkas-list"),
    path('berkas/<int:pk>/', BerkasUpdateDelete.as_view(), name= "berkas-details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)