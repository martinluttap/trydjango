import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    timestamp = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.answer_text
