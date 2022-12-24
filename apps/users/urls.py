from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, UserDetailApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=UserApiViewSet
)

router.register(
    prefix="",
    viewset=UserDetailApiViewSet
)

urlpatterns = router.urls
