from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from django.core import serializers
from .models import *


def graph(request):
    return render(request, 'graph/graph.html')


def play_count_by_month(request):
    data = Play.objects.all() \
        .extra(
            select={
                'month': connections[Play.objects.db].ops.date_trunc_sql('month', 'date')
            }
        ) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)


def get_sample_data(request):
    data = Result.objects.all()
    array = []
    for obj in data:
        temp = {
            'employee': obj.employee.name,
            'first': obj.first,
            'second': obj.second,
            'third': obj.third,
        }
        array.append(temp)
    return JsonResponse(list(array), safe=False)

