from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


def all_orders(request):
    orders = Order.get_all()
    return render(request, 'order/order_list.html',
                  {
                      'title': "Orders",
                      'heading': "All Orders",
                      "orders": orders
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
