# urls.py
from rest_framework.routers import DefaultRouter
from .views import IdeViewSet

router = DefaultRouter()
router.register(r'ide', IdeViewSet, basename='ide')

urlpatterns = router.urls
