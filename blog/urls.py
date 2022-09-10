from .views import RegionViewSet, ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'region/', RegionViewSet, basename='region')
router.register(r'contact/', ContactViewSet, basename='contact')
urlpatterns = router.urls


AUTH_USER_MODEL = ''

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTIFICATION_CLASSES':[
        'rest_framework.authentification.TokenAuthentification',
        'rest_framework.authentification.BasicAuthentification',
        'rest_framework.authentification.SessionAuthentification',
    ],
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.authentification.iSAuthentification',
    ],
}