from django.urls import path

from apps.chats.views import ChatApiView


urlpatterns = [
    path('chats/', ChatApiView.as_view())
]
