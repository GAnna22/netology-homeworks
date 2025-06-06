from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    context = {'phones': phone_objects}
    # phones = [f'{c.id}: {c.slug}, {c.price}' for c in phone_objects]
    # return HttpResponse('<br>'.join(phones))
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
