from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from rest_framework import routers

from .views import OrderByUserIdView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user/<pk>/order', include(router.urls), name='user-orders'),

    path('', views.all_users, name='users'),
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
]