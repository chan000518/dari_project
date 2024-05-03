from django.views.generic import ListView
from .models import Interview
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Interview, InterviewQuestion
from .forms import InterviewForm # InterviewForm은 커스텀 폼으로 질문 선택 로직을 포함해야 합니다.
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Interview


class InterviewListView(ListView):
    model = Interview
    template_name = 'interview/interview_list.html'
    context_object_name = 'interviews'

    def get_queryset(self):
        return Interview.objects.filter(created_by=self.request.user)


class InterviewCreateView(CreateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'interview/interview_form.html'
    
    def form_valid(self, form):
        # 인터뷰 인스턴스를 먼저 데이터베이스에 저장
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        form.save_m2m()

        # 인터뷰가 데이터베이스에 저장된 후, Many-to-Many 관계를 설정
        self.object.questions.clear()  # 기존에 연결된 질문들을 제거 (업데이트 시 필요)
        questions = form.cleaned_data['questions']
        for question in questions:
            InterviewQuestion.objects.create(interview=self.object, question=question)  # 순서 설정 필요

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('interview:interview_list')

class InterviewDetailView(DetailView):
    model = Interview
    template_name = 'interview/interview_detail.html'
    context_object_name = 'interview'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 인터뷰와 연결된 모든 질문을 가져오기 위해, ManyToMany 필드를 활용
        context['questions'] = self.object.questions.all()
        return context

class InterviewUpdateView(UpdateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'interview/interview_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Update existing InterviewQuestion instances or create new ones
        return response
    def test_func(self):
        # 현재 인터뷰의 생성자가 요청을 보낸 사용자와 같은지 확인
        obj = self.get_object()
        return obj.created_by == self.request.user

    def get_success_url(self):
        return reverse_lazy('interview:interview_list')

class InterviewDeleteView(DeleteView):
    model = Interview
    template_name = 'interview/interview_delete.html'
    
    def test_func(self):
        # 현재 인터뷰의 생성자가 요청을 보낸 사용자와 같은지 확인
        obj = self.get_object()
        return obj.created_by == self.request.user

    def get_success_url(self):
        # 인터뷰 삭제 후 인터뷰 목록 페이지로 리디렉션
        return reverse_lazy('interview:interview_list')

