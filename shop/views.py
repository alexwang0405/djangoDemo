from django.shortcuts import render
from .models import Shop
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def shop(request):
	# shop_list = Shop.objects.all().order_by('price')
	name=''
	startp=''
	endp=''
	acer=''
	asus=''
	lenovo=''

	if 'product' in request.GET:
		name = request.GET['product']
		startp = request.GET['startp']
		endp = request.GET['endp']
		# 必須使用get給予預設值 否則會出現 MultiValueDictKeyError
		acer = request.GET.get('acer', '')
		asus = request.GET.get('asus', '')
		lenovo = request.GET.get('lenovo', '')
		
		if acer=='' and asus=='' and lenovo=='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp).order_by('price')
		elif acer!='' and asus=='' and lenovo=='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name, brand=acer).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp, brand=acer).order_by('price')
		elif acer=='' and asus!='' and lenovo=='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name, brand=asus).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp, brand=asus).order_by('price')
		elif acer=='' and asus=='' and lenovo!='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name, brand=lenovo).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp, brand=lenovo).order_by('price')
		elif acer!='' and asus!='' and lenovo=='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name, brand__in=[acer,asus]).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp, brand__in=[acer,asus]).order_by('price')
		elif acer!='' and asus=='' and lenovo!='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name, brand__in=[acer,lenovo]).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp, brand__in=[acer,lenovo]).order_by('price')
		elif acer=='' and asus!='' and lenovo!='':
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name, brand__in=[lenovo,asus]).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp, brand__in=[lenovo,asus]).order_by('price')
		else:
			if startp == '' and endp == '':
				shop_list = Shop.objects.all().filter(title__icontains=name).order_by('price')
			else:
				shop_list = Shop.objects.all().filter(title__icontains=name, price__gte=startp, price__lte=endp).order_by('price')
	else :
		shop_list = Shop.objects.all().order_by('price')
	
	# 每一頁最多20個
	paginator = Paginator(shop_list, 20)
	page = request.GET.get('page')
	try:
		pageContent = paginator.page(page)
	except PageNotAnInteger:
		pageContent = paginator.page(1)
	except EmptyPage:
		pageContent = paginator.page(paginator.num_pages)
	
	content = {'shop_list':pageContent, 'startp':startp, 'endp':endp, 'product':name,'acer': acer, 'asus': asus, 'lenovo': lenovo }
	return render(request, 'shop.html', content)
