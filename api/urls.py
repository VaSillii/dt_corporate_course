from django.urls import path

from .views import ClassificationTextAPIView

app_name = 'api'

urlpatterns = [
    path('label/', ClassificationTextAPIView.as_view()),
]
