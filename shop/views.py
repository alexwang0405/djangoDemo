from django.shortcuts import render
from .models import Shop
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def shop(request):
	# shop_list = Shop.objects.all().order_by('price')
	name=''
	startp=''
	endp=''
	brand=''
	brandName = Shop.objects.values('brand').distinct()
	
	if 'brand' in request.GET:
		brand = request.GET['brand']
		shop_list = Shop.objects.filter(brand = brand).order_by('price')
		if 'product' in request.GET:
			name = request.GET['product']
			startp = request.GET['startp']
			endp = request.GET['endp']
			if startp == '' and endp == '':
				shop_list = Shop.objects.filter(brand=brand, title__icontains=name).order_by('price')
			else:
				shop_list = Shop.objects.filter(brand=brand, title__icontains=name, price__gte=startp, price__lte=endp).order_by('price')
	else :
		shop_list = Shop.objects.all().order_by('price')
	
	#else:
		#shop_list = Shop.objects.all().order_by('price')
	# 每一頁最多20個
	paginator = Paginator(shop_list, 20)
	page = request.GET.get('page')
	try:
		pageContent = paginator.page(page)
	except PageNotAnInteger:
		pageContent = paginator.page(1)
	except EmptyPage:
		pageContent = paginator.page(paginator.num_pages)
	
	content = {'shop_list':pageContent, 'startp':startp, 'endp':endp, 'product':name, 'brandName':brandName,'brand':brand }
	return render(request, 'shop.html', content)
