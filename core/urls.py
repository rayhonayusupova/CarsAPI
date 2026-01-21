from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import SignUpView,PublicCarViewSet, UserCarViewSet

router = DefaultRouter()
router.register('public/cars', PublicCarViewSet, basename='public-cars')
router.register('my/cars', UserCarViewSet, basename='my-cars')

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/sign-up/',SignUpView.as_view(),name='sing_up'),
    path('api/',include(router.urls), name='cars')
    
]