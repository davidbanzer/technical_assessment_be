from .views import StringsProblemView
from django.urls import path


urlpatterns = [
    path('string-problem/', StringsProblemView.as_view()),

]