from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
        {'href': 'index', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукт'},
        {'href': 'about', 'name': 'О нас'},
        {'href': 'contacts', 'name': 'Контакты'},
    ]

def products(request):
    title = "продукты"

    products = Product.objects.all().order_by('-price')
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'categories': categories,
    }

    return render(request, 'products.html', context)

def product(request, pk):
    title = "продукт"

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'category': category,
    }

    return render(request, 'product.html', context)
