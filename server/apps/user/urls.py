from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('edit/', UserEditView.as_view(), name='edit_profile'),
    path('delete/', UserDeleteView.as_view(), name='delete_user'),
]
