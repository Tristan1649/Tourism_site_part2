from .views import RegionViewSet, ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'region/', RegionViewSet, basename='region')
router.register(r'contact/', ContactViewSet, basename='contact')
urlpatterns = router.urls