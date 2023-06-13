from .views import StringsProblemView, ChessProblemView
from django.urls import path


urlpatterns = [
    path('string-problem/', StringsProblemView.as_view()),
    path('chess-problem/', ChessProblemView.as_view()),
]