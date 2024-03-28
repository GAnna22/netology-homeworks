from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import pandas as pd
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))

CONTENT = pd.read_csv(settings.BUS_STATION_CSV)

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 20)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': CONTENT.iloc[20*(page_number-1):20*page_number],
        'page': page,
    }
    return render(request, 'stations/index.html', context)
