from django.shortcuts import render

links_menu = [
        {'href' : 'index', 'name': 'Главная'},
        {'href' : 'products:index', 'name': 'Продукт'},
        {'href' : 'about', 'name': 'О нас'},
        {'href' : 'contacts', 'name': 'Контакты'},
    ]

def products(request):
    title = "продукты"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'products.html', context)
