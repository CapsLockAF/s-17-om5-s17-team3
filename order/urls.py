from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_orders, name='orders'),
    path('<int:id>/', views.order_form, name='order'),
    path('<int:id>/delete/', views.order_delete, name='order_delete'),
    path('<int:id>/view/', views.order_view, name='order_by_id'),
]