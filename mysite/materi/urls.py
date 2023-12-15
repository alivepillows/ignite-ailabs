# urls.py
from django.urls import path 
from .views import MateriList, MateriUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('materi/', MateriList.as_view(), name= "create-materi-list"),
    path('materi/<int:pk>/', MateriUpdateDelete.as_view(), name= "materi-details")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)