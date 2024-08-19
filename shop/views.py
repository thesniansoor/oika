from django.shortcuts import render
from .models import Category, Product, SubCategory

# Create your views here.

def home(request):
   # return render(request,"index.html")
    products=Product.objects.all() 
    categories = Category.objects.all()
    sub_categories=SubCategory.objects.all() 
    return render(request,'home.html',{'products':products,'categories': categories,'sub_categories': sub_categories}) # type: ignore

# def home(request):
#    return render(request,"home.html")
    



def product_list(request):
    products=Product.objects.all() 
    categories = Category.objects.all()
    sub_categories=SubCategory.objects.all() 
    return render(request,'product_list.html',{'products':products,'categories': categories,'sub_categories': sub_categories}) # type: ignore
