# interviews/urls.py
from django.urls import path
from .views import *

app_name = 'interview'

urlpatterns = [
    path('', InterviewListView.as_view(), name='interview_list'),
    path('create/', InterviewCreateView.as_view(), name='interview_create'),
    path('<int:pk>/update/', InterviewUpdateView.as_view(), name='interview_update'),
    path('<int:pk>/delete/', InterviewDeleteView.as_view(), name='interview_delete'),
    path('interview/<int:pk>/', InterviewDetailView.as_view(), name='interview_detail'),
]
