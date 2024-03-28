from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def omlet_view(request):
    context = {}
    portion_number = int(request.GET.get("servings", 1))
    context['recipe'] = {}
    for k, v in DATA['omlet'].items():
        context['recipe'][k] = portion_number * v
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    context = {}
    portion_number = int(request.GET.get("servings", 1))
    context['recipe'] = {}
    for k, v in DATA['pasta'].items():
        context['recipe'][k] = portion_number * v
    return render(request, 'calculator/index.html', context)

def butter_view(request):
    context = {}
    portion_number = int(request.GET.get("servings", 1))
    context['recipe'] = {}
    for k, v in DATA['butter'].items():
        context['recipe'][k] = portion_number * v
    return render(request, 'calculator/index.html', context)

def home_view(request):
    return HttpResponse('HELLO!')