from django.shortcuts import render


def main(request):
    context = {
        'name': 'Anton',
        'my_list': [
            1,3,4,5
        ]
    }
    return render(request, 'mainapp/index.html',context)

def products(request):
    context = {
        'name': 'Задачи',
        'my_list': [
            "Ветвление", "Циклы", "Линейные", "сортировка"
        ]
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')
