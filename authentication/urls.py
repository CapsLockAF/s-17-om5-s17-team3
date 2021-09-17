from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_users, name='users'),
    # path('<int:id>', views.view_user, name='user'),
    # path('form/', views.user_form, name='user_form'),
    # path('update/<int:id>', views.uodate_user_form, name='update_form'),
    # path('delete/<int:id>', views.delete_user_form, name='delete_form'),
]