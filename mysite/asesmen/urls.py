# urls.py
from django.urls import path 
from .views import AsesmenListView, AsesmenUpdateDeleteView, PivotAsesmenListView, PivotAsesmenUpdateRetrieveDelete, SubAsesmenList, SubAsesmenUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('asesmen/', AsesmenListView.as_view(), name= "create-asesmen-list"),
    path('asesmen/<int:pk>/', AsesmenUpdateDeleteView.as_view(), name= "subasesmen-details"),
    path('pivotasesmen/', PivotAsesmenListView.as_view(), name= "create-asesmen-list"),
    path('pivotasesmen/<int:pk>/', PivotAsesmenUpdateRetrieveDelete.as_view(), name= "subasesmen-details"),
    path('subasesmen/', SubAsesmenList.as_view(), name= "create-asesmen-list"),
    path('subasesmen/<int:pk>/', SubAsesmenUpdateDelete.as_view(), name= "subasesmen-details"),
    # path('getvalue/', CalculateAsesmentValue.as_view(), name="get-value-asesment")    
]