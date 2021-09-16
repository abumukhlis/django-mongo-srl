from rest_framework import routers

from .views import DecksViewSet

router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
router.register('', DecksViewSet)
urlpatterns = router.urls