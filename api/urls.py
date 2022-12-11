from django.urls import path
from .views import AutoCostPredict


urlpatterns = [
    path('', AutoCostPredict.as_view()),
]