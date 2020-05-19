from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django import forms
from resume.models import Resume
from vacancy.models import Vacancy
from django.core.exceptions import PermissionDenied


class MenuView(View):
    def get(self, request):
        return render(request, 'menu.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    template_name = "login.html"


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = "signup.html"


class Profile(View):
    def get(self, request):
        return render(request, 'profile.html')


class ResumeForm(forms.Form):
    description = forms.CharField(max_length=1024)


class NewResumeView(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, 'new_resume.html', {'form': form})

    def post(self, request):
        form = ResumeForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                description = form.cleaned_data["description"]
                Resume.objects.create(description=description, author=request.user)
            return redirect('home')
        else:
            raise PermissionDenied


class VacancyForm(forms.Form):
    description = forms.CharField(max_length=1024)


class NewVacancyView(View):
    def get(self, request):
        form = VacancyForm()
        return render(request, 'new_vacancy.html', {'form': form})

    def post(self, request):
        form = ResumeForm(request.POST)
        if request.user.is_staff:
            if form.is_valid():
                description = form.cleaned_data["description"]
                Vacancy.objects.create(description=description, author=request.user)
            return redirect('home')
        else:
            raise PermissionDenied


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

