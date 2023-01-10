from django.urls import path

from apps.message.views import MessageApiView


urlpatterns = [
    path('message/', MessageApiView.as_view())
]
