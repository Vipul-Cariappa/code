from django.urls import path, include
from . import views

app_name = "challenge"


urlpatterns = [
    path('', views.index, name='home'),
    path('new-question', views.question_new, name='new-question'),
    path('list-question', views.question_list, name='list-question'),
    path('view-answer/<int:answer_id>', views.answer_view, name='view-answer'),
    path('list-answers/<int:question_id>',
         views.result_answer, name='results'),
    path('test-answer/<int:question_id>',
         views.answer_test, name='new-question'),
    path('answer/<int:question_id>', views.answer, name='answer'),
    path('failed', views.fail, name='fail'),
]
