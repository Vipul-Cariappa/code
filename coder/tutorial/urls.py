from django.urls import path, include
from . import views

app_name = "tutorial"


urlpatterns = [
    path('functions', views.functions, name='home'),
]
