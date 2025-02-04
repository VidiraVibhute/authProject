from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'registration.html'  
    form_class = UserCreationForm  
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        return redirect(self.success_url)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm  

    def get_success_url(self):
        return reverse_lazy('dashboard')  


class DashboardView(TemplateView):
    template_name = 'dashboard.html' 


def custom_logout_view(request):
    logout(request)
    return redirect('login')
