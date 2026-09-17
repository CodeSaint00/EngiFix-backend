from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from departments.views import DepartmentViewSet
from locations.views import LocationViewSet
from equipment.views import EquipmentViewSet
from faults.views import FaultReportViewSet
from maintenance.views import MaintenanceRecordViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'faults', FaultReportViewSet)
router.register(r'maintenance', MaintenanceRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]