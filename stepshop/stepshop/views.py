from django.shortcuts import render

from mainapp.models import Product

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукт', 'route': 'products/'},
    {'href': 'about', 'name': 'О нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def index(request):
    title = "Главная"

    products = Product.objects.all()
    # categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        # 'categories': categories,
    }

    return render(request, 'index.html', context)


def contacts(request):
    title = "контакты"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'contacts.html', context)


def about(request):
    title = "о нас"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'about.html', context)


def products(request):
    title = "продукты"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'products.html', context)


def product(request):
    title = "товар"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'product.html', context)
