from django.shortcuts import render
from django.http import JsonResponse
from .models import Category,Product
# Create your views here.

def products_list(request):
    products = Product.objects.all()
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
        })
    return JsonResponse(data, safe=False)

def products_detail(request, id):
    product = Product.objects.get(id=id)
    return JsonResponse({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
    })
def categories_list(request):
    categories = Category.objects.all()
    data = []
    for c in categories:
        data.append({
            'id': c.id,
            'name': c.name,
        })
    return JsonResponse(data, safe=False)
def categories_detail(request, id):
    category = Category.objects.get(id=id)
    return JsonResponse({
        'id': category.id,
        'name': category.name,
    })

def category_products(request, id):
    products = Product.objects.get(category_id=id)
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
        })
    return JsonResponse(data, safe=False)
