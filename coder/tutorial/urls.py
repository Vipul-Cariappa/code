from django.urls import path, include
from . import views

app_name = "tutorial"


urlpatterns = [
    path('functions', views.functions, name='functions'),
    path('io', views.io, name='io'),
    path('intro', views.intro, name='intro'),
    path('variables', views.variables, name='variables'),
    path('if_statements', views.if_statements, name='if_statements'),
    path('loops', views.loops, name='loops'),
]
