from rest_framework.routers import DefaultRouter

from houses import views


router = DefaultRouter()
router.register(r'houses', views.HouseViewSet)

urlpatterns = router.urls