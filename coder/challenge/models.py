from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question = models.TextField()
    solution = models.TextField()
    test_case = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    time = models.FloatField()
    memory = models.IntegerField()
    character = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
