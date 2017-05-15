from django.shortcuts import render
from .models import About

def about(request):
    context = {'content': About.objects.first().content}
    return render(request, 'about/about.html', context)