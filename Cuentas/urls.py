from django.urls import path
from . import views
from .views import CustomUserRegister
from . import forms
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    # login, logout, register
    path('signup/', CustomUserRegister.as_view(), name='signup'),
    path('', LoginView.as_view(template_name='home.html', authentication_form=forms.CustomAuthForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # list_views
    path('alumni/', views.alumni_list_view, name='alumni'),
    path('profesores/', views.profesor_list_view, name='profesores'),
    path('all_users/', views.all_users_list_view, name='all_users'),

]