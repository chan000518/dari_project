from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions/question_list.html'

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'question/question_detail.html'

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_text']
    template_name = 'question/question_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question_text']
    template_name = 'question/question_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Question = self.get_object()
        return Question.created_by == self.request.user

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    context_object_name = 'question'
    template_name = 'question/question_delete.html'
    success_url = reverse_lazy('question_list')

    def test_func(self):
        Question = self.get_object()
        return Question.created_by == self.request.user
