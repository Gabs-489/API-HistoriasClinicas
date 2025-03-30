from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoriaClinicaViewSet

router = DefaultRouter()
router.register(r'historias', HistoriaClinicaViewSet)

urlpatterns = [
    path('api/historias_clinicas/', include(router.urls)),
]

