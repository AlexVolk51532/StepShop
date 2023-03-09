from django.shortcuts import render

from mainapp.models import Product, ProductCategory

links_menu = [
        {'href' : 'index', 'name': 'Главная'},
        {'href' : 'products:index', 'name': 'Продукт'},
        {'href' : 'about', 'name': 'О нас'},
        {'href' : 'contacts', 'name': 'Контакты'},
    ]

def products(request):
    title = "продукты"

    products = Product.objects.all()[:2]
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'categories': categories,
    }

    return render(request, 'products.html', context)
