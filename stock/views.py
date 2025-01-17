from django.shortcuts import render
from .models import Stock

# Create your views here.

def stock(request):
	names = Stock.objects.values('name','no').distinct()
	name=''
	if 'stockname' in request.POST:
		stockname = request.POST['stockname']
		name = stockname.split('(')[0]
		if 'date' in request.POST:
			date = request.POST['date']
			y,m = date.split('-')
			y = int(y)-1911
			date = str(y)+m
			items = Stock.objects.filter(name=name, date__icontains=date).order_by('date')
		else:
			items = Stcok.objects.filter(name=name).order_by('id')
	else:
		items=[]
	date=[]
	openprice=[]
	endprice=[]
	for item in items:
		d = int(item.date)
		date.append(d%100)
		openprice.append(item.openprice)
		endprice.append(item.endprice)
	content = {'names':names, 'items':items, 'stockname':name, 'openprice':openprice, 'endprice':endprice, 'date':date}
	return render(request, 'stock.html', content)
