from django.shortcuts import render
# from prose.models import ProjitoeNeUgasaet
from django.views.generic import DetailView, ListView


def main_page(request):
    return render(request, 'flatpages/default.html')


def get_about_info(request):
    return render(request, 'flatpages/about.html')