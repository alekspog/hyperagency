from django.shortcuts import render
from django.views import View
from .models import Resume


class ResumeView(View):
    def get(self, request):
        return render(request, 'resumes.html', {'resumes': Resume.objects.all()})
