from django.urls import path
from .views import *

app_name = 'question'

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('create/', QuestionCreateView.as_view(), name='question_create'),
    path('update/<int:pk>/', QuestionUpdateView.as_view(), name='question_update'),
    path('delete/<int:pk>/', QuestionDeleteView.as_view(), name='question_delete'),
]
