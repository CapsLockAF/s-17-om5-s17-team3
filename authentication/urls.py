from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_users, name='users'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
=======
    # path('<int:id>', views.view_user, name='user'),
    # path('form/', views.user_form, name='user_form'),
    # path('update/<int:id>', views.uodate_user_form, name='update_form'),
    # path('delete/<int:id>', views.delete_user_form, name='delete_form'),
>>>>>>> 119b1d6 (add[User]: base url in main settings, output list of users)
=======
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
>>>>>>> 4d977ed (add[User]: a form for creating user, methods, templates, urls, etc.)
]