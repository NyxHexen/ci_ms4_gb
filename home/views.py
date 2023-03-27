from django.shortcuts import render
from django.db.models import Max
from games.models import Game, DLC
from promo.models import Promo
import datetime as dt

import random


def index(request):
    """ A view to return the index page """
    carousel = list(Game.objects.filter(carousel=True))
    carousel += list(Promo.objects.filter(carousel=True))
    carousel += list(DLC.objects.filter(carousel=True))

    is_featured = list(Game.objects.filter(is_featured=True))
    if len(is_featured) > 4:
        is_featured = random.sample(is_featured, 6)
    
    dotd = list(Promo.objects.filter(active=True, landing_page=True))

    for promo in dotd:
        promo_games = promo.apply_to_game.all().aggregate(Max('promo_percentage')).get('promo_percentage__max', 0)
        promo_dlc = promo.apply_to_dlc.all().aggregate(Max('promo_percentage')).get('promo_percentage__max', 0)
        highest_promo_percentage = max(
            promo_games if promo_games is not None else 0, 
            promo_dlc if promo_dlc is not None else 0)
        promo.promo_percentage = highest_promo_percentage

    if len(dotd) < 4:
        dotd_topup = list(Game.objects.filter(in_promo=True, promo__active=True, promo__landing_page=False))
        dotd_topup += list(DLC.objects.filter(in_promo=True, promo__active=True, promo__landing_page=False))
        dotd_topup = sorted(dotd_topup, key=lambda x: x.promo.end_date)
        dotd = dotd + dotd_topup[:4 - len(dotd)]

    print(dotd)

    context = {
        'carousel': carousel,
        'is_featured': is_featured,
        'dotd': dotd
    }
    return render(request, 'home/index.html', context)