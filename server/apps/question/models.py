from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class Question_archive(models.Model):
    question_text = models.TextField()  # 질문 내용
    
    def __str__(self):
        return self.question_text


class Question(models.Model):
    question_text = models.TextField()  # 질문 내용
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 질문 생성자
    created_at = models.DateTimeField(default=timezone.now)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 마지막 수정 시간

    def __str__(self):
        return self.question_text
    
    def get_absolute_url(self):
        return reverse('question_list')
