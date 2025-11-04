from rest_framework import routers
from .views import VisitorViewSet, OfficeViewSet, VisitViewSet


router = routers.DefaultRouter()
router.register(r'visitors', VisitorViewSet)
router.register(r'offices', OfficeViewSet)
router.register(r'visits', VisitViewSet)


urlpatterns = router.urls