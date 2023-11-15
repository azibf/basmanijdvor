from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(category=item.category).exclude(pk=id)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
