from django.urls import path
from rendercv import views

urlpatterns = [
    path('', views.cv)
]
