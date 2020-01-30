from django.urls import path, include
from . import views
from .views import Another

from rest_framework import routers
from .views import CarViewSet

router = routers.DefaultRouter()
router.register('cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('first', views.first),
    path('second', views.second),
    path('another', Another.as_view())
]