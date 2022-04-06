from django.shortcuts import render
from django.http import HttpResponse


def load_brand_file(request):
    return HttpResponse('We loaded the brand file (not really)')

