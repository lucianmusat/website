from django.shortcuts import render
from .models import Index

def index(request):
    context = {'content': Index.objects.first().content}
    return render(request, 'index/index.html', context)