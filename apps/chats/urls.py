from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatApiViewSet, ChatCreateApiViewSet


router = DefaultRouter()
router.register(
    prefix="chat",
    viewset=ChatApiViewSet
)

router.register(
    prefix="create",
    viewset=ChatCreateApiViewSet
)

urlpatterns = router.urls
