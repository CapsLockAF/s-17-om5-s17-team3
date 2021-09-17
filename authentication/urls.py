from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_users, name='users'),
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
]