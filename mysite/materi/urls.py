# urls.py
from django.urls import path 
from .views import MateriList, MateriUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('materi/', MateriList.as_view(), name= "create-materi-list"),
    path('materi/<int:pk>/', MateriUpdateDelete.as_view(), name= "materi-details")
]