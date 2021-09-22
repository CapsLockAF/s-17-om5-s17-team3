from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.core.paginator import Paginator

from rest_framework import viewsets
from .serializers import OrderSerializer

num_items = 5


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def all_orders(request):
    orders = Order.get_all()
    paginator = Paginator(orders, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, 'order/order_list.html',
                  {
                      'title': "Orders",
                      'heading': "All Orders",
                      'page_obj': page_obj,
                      'page_nums': page_nums,
                  })


def order_view(request, id=0):
    order_by_id = Order.get_by_id(id)
    return render(request, 'order/order_view.html',
                  {
                      'title': "Order",
                      'heading': "Order Info",
                      "order_by_id": order_by_id
                  })


def order_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
            return render(request, 'order/order_form_add.html', {'form': form})
        else:
            order = Order.objects.get(id=id)
            form = OrderForm(instance=order)
            return render(request, 'order/order_form.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(id=id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('orders')


def order_delete(request, id=0):
    order = Order.get_by_id(id)
    order.delete()
    orders = Order.get_all()
    return render(request, 'order/order_list.html',
                  {
                      'title': "All orders",
                      "orders": orders
                  })
