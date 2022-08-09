from django.http import HttpResponse
from django.shortcuts import render, redirect
from food.models import Item
from food.forms import ItemForm
# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list,
    }
    return render(request, 'food/index.html', context=context)


def item(request):
    return HttpResponse("This is an item view")


def detail(request, id=None):
    item = Item.objects.get(pk=id)
    context = {
        "item": item
    }

    return render(request, 'food/details.html', context=context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', context={
        "form": form
    })


def update(request, id=None):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', context={
        'form': form,
        'item': item
    })


def delete(request, id=None):
    item = Item.objects.get(pk=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete.html', context={
        "item": item
    })
