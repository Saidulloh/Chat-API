from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatApiViewSet


router = DefaultRouter()
router.register(
    prefix="chats",
    viewset=ChatApiViewSet
)

urlpatterns = router.urls
