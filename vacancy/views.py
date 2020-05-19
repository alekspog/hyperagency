from django.views import  View
from django.shortcuts import render
from .models import Vacancy


class VacancyView(View):
    def get(self, request):
        return render(request, "vacancies.html", {'vacancies': Vacancy.objects.all()})
