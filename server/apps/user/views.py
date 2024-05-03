from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'

class UserEditView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('login')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 로그인한 유저가 있다면, 유저 이름을 컨텍스트에 추가
        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username
        return context
