from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(reuest):
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(reuest,'myapp/index.html',{'all_customers':customers,'all_products':products})

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        product_id = request.POST['product_id']
        print("==================",product_id)
        myshowPrice = request.POST['myshowPrice']
        qty = request.POST['qty']
        total = request.POST['total']
        print(customer_id)
        customer_id = Customer.objects.get(id=int(customer_id))
        product_id = Product.objects.get(id=int(product_id))
        print("==================",customer_id)
        print("==================",product_id)
        Order.objects.create(
            customer_Id=customer_id,product_Id=product_id,unit_Price=myshowPrice,Quntity=qty,total_Price=total)
        return JsonResponse({'status':'Success'})

def order_list(request):
    all_order = Order.objects.all()
    return render(request,'myapp/orderlist.html',{'all_order':all_order})

def search(request):
    query = request.GET['search']
    allProd = Order.objects.filter(customer_Id__fName__contains=query)
    return render(request,'myapp/orderlist.html',{'all_order':allProd})