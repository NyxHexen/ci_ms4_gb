from django.shortcuts import render
from django.http import QueryDict
from django.core.paginator import Paginator, EmptyPage
from urllib.parse import urlencode

from games.models import (Game, Genre,
                          Tag, Platform, Feature, DLC)
from .utils import sort_by

from decimal import Decimal
from datetime import datetime


def games(request):
    games = Game.objects.all()
    dlcs = DLC.objects.all()

    filter_dict = QueryDict(mutable=True)

    if "filter" in request.GET:
        """
        Lambda is an anonymous function, by defining a dictionary which holds a query key as a key received via request.GET
        passed on from the filter form and a value which is a function, it allows us to easily filter sets
        by running them through a for loop and using value(queryset, param) to apply the filter.
        The dictionary structure of the filter also improves readability, so long lambda functions are kept simple,
        and maintainability.
        """
        filter_condition = {
            "sale_only": lambda queryset, *args: queryset.filter(
                in_promo=True, promo__active=True
            ),
            "hide_extras": lambda queryset, *args: queryset.exclude(
                required_game__isnull=False
            )
            if all(hasattr(obj, "required_game") for obj in queryset.all())
            else queryset,
            "price_range": lambda queryset, param: queryset.filter(
                final_price__gte=Decimal(param[0]), final_price__lte=Decimal(param[1])
            )
            if len(param) == 2
            else queryset,
            "genres_filter": lambda queryset, param: queryset.filter(
                genres__slug__in=param
            ).distinct()
            if not all(hasattr(obj, "required_game") for obj in queryset.all())
            else queryset.filter(required_game__genres__slug__in=param).distinct(),
            "tags_filter": lambda queryset, param: queryset.filter(
                tags__slug__in=param
            ).distinct(),
            "platforms_filter": lambda queryset, param: queryset.filter(
                platforms__slug__in=param
            ).distinct()
            if not all(hasattr(obj, "required_game") for obj in queryset.all())
            else queryset.filter(required_game__platforms__slug__in=param).distinct(),
            "features_filter": lambda queryset, param: queryset.filter(
                features__slug__in=param
            ).distinct(),
            "date_range": lambda queryset, param: queryset.filter(
                release_date__gte=datetime(int(param[0]), 1, 1),
                release_date__lte=datetime(int(param[1]), 12, 31),
            )
            if len(param) == 2
            else queryset,
        }

        filtered_games = games
        filtered_dlcs = dlcs

        for key, value in filter_condition.items():
            if key in request.GET:
                if filter_dict.get(key) is None:
                    filter_dict.update({f"{key}": f"{request.GET.get(key)}"})
                filter_param = (
                    request.GET.getlist(key)[0].split(",")
                    if key.endswith("_filter") or key.endswith("_range")
                    else request.GET.get(key)
                )

                filtered_games = (
                    value(games, filter_param) if len(games) > 0 else list()
                )
                filtered_dlcs = value(dlcs, filter_param) if len(dlcs) > 0 else list()

        if "sort_by" in request.GET:
            filter_dict.update({f"sort_by": f'{request.GET.get("sort_by")}'})

        filtered_results = sort_by(
            request.GET.get("sort_by"), filtered_games, filtered_dlcs
        )
        paginator = Paginator(filtered_results, 20)
    else:
        if "sort_by" in request.GET:
            filter_dict.update({f"sort_by": f'{request.GET.get("sort_by")}'})
        sorted_games = sort_by(request.GET.get("sort_by"), games, dlcs)
        paginator = Paginator(sorted_games, 20)

    page_number = request.GET.get("page")

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.get_page(paginator.num_pages)

    paginator_iter = range(1, page.paginator.num_pages + 1)

    genres = Genre.objects.all()
    tags = Tag.objects.all()
    platforms = Platform.objects.all()
    features = Feature.objects.all()

    context = {
        "page": page,
        "paginator_iter": paginator_iter,
        "genres": genres,
        "tags": tags,
        "platforms": platforms,
        "features": features,
    }

    if "filter" in request.GET:
        items = filtered_results or list(games) + list(dlcs)
    else:
        items = sorted_games or list(games) + list(dlcs)

    context["price_slider_ceil"] = float(
        max(items, key=lambda item: item.final_price).final_price
    )

    if "filter" in request.GET or "sort_by" in request.GET:
        context["filter_dict"] = urlencode(filter_dict)
    
    return render(request, "games/index.html", context)


def game(request, model_name, game_id):
    game = Game.objects.get(id=game_id) if model_name == 'game' else DLC.objects.get(id=game_id)
    media = game.media.exclude(name__icontains='COVER')

    context = {
        'game': game,
        'media': media
    }
    return render(request, "games/game.html", context)