from django.db import models
from django.conf import settings
from ..question.models import Question
# Create your models here.
class Interview(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, through='InterviewQuestion')

    def __str__(self):
        return self.title

class InterviewQuestion(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}. {self.question.question_text}"