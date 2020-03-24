from django.shortcuts import render
from .models import Book
# Create your views here.

def book(request):
	items = Book.objects.values('kind').distinct()
	
	if 'kind' in request.GET:
		kind = request.GET['kind']
		allData = Book.objects.all().filter(kind=kind)
	else:
		allData = Book.objects.all().order_by('price')
		
	content = {'items': items, 'allData':allData}
	return render(request, 'book.html', content)
