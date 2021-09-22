from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('<int:user_id>/order/', include(router.urls)),

    path('', views.all_users, name='users'),
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
]