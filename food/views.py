from django.shortcuts import render
from .models import Food

# Create your views here.

def food(request):
	allData = Food.objects.all().order_by('-datetime')
	return render(request, 'food.html', {'allData':allData})
	
