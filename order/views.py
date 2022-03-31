from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Watch
from .models import Order
from order.forms import CreateOrderForm


def create_order(request, watch_id):
    watch = Watch.objects.get(id=watch_id)
    print(request.POST)
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        print(order_form.cleaned_data)
        # order = Order.objects.create(**order_form.cleaned_data)
        order_form.save()
        return redirect(watch.get_absolute_url)
    order_form = CreateOrderForm()
    return render(request, 'order/order.html', {'form': order_form,
                                                'watch': watch})

