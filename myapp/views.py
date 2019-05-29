import os
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from djdatatableview.tables_new import TableView
# Create your views here.


def index(request):
    context = dict(
        table_a=TableView(id='table_a', url='/test1', columns=['a', 'b', 'c', 'd']),
        table_b=TableView(id='table_b', url='/test2', columns=['x', 'y', 'z'])
    )
    return render(request, os.path.join('index.html'), context)


def test1(request):
    return JsonResponse({
        'data': [
            {'a': 1, 'b': 2, 'c': 3, 'd': 4},
            {'a': 2, 'b': 3, 'c': 4, 'd': 1},
            {'a': 3, 'b': 4, 'c': 1, 'd': 2},
            {'a': 4, 'b': 1, 'c': 2, 'd': 3}
        ]
    }, safe=False)


def test2(request):
    return JsonResponse({
        'data': [
            dict(x=1, y=2, z=3),
            dict(x=2, y=3, z=4),
            dict(x=3, y=4, z=1),
        ]
    }, safe=False)
