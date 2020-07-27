from django.urls import path
from . import views

urlpatterns = [
    path('', views.questao, name='questao'),
]