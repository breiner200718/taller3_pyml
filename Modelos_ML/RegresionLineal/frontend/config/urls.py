from django.urls import path
from predictor.views import home

urlpatterns = [
    path("", home, name="home"),
]
