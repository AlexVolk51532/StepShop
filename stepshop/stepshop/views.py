from django.shortcuts import render

from mainapp.models import Product
from mainapp.views import get_basket

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def index(request):
    title = "Главная"

    products = Product.objects.all()
    # categories = ProductCategory.objects.all()
    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'basket': basket,
        # 'categories': categories,
    }

    return render(request, 'index.html', context)


def contacts(request):
    title = "контакты"

    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket,
    }

    return render(request, 'contacts.html', context)


def about(request):
    title = "о нас"

    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket,
    }

    return render(request, 'about.html', context)
