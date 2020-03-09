from django.shortcuts import render
from .models import Home
# Create your views here.

def home(request):
    allData = Home.objects.all()
    content = {'allData': allData}
    return render(request, 'index.html', content)
