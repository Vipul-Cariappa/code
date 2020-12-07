from django.urls import path, include
from . import views

app_name = "challenge"


urlpatterns = [
    path('', views.index, name='home'),
    path('new-question', views.question_new, name='new-question'),
    path('answer/<int:question_id>', views.answer, name='answer'),
    path('failed', views.fail, name='fail'),
]
