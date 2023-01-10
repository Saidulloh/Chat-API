from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, UserDetailApiViewSet


router = DefaultRouter()
router.register(
    prefix="users",
    viewset=UserApiViewSet
)

router.register(
    prefix="user",
    viewset=UserDetailApiViewSet
)

urlpatterns = router.urls
