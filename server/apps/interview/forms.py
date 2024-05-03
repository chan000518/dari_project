from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Interview, InterviewQuestion
from ..question.models import Question

class InterviewForm(ModelForm):
    questions = ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Interview
        fields = ['title', 'questions']

    
    def save(self, commit=True):
        interview = super().save(commit=False)
        if commit:
            interview.save()
        if interview.pk:
            interview.questions.clear()  # 기존 질문을 제거
            # 선택된 질문을 InterviewQuestion을 통해 추가
            for question in self.cleaned_data['questions']:
                InterviewQuestion.objects.create(
                    interview=interview,
                    question=question,
                )
        return interview
