from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_authors, name='authors'),
    path('form/', views.author_form, name='author_form'),
    path('form/<int:id>', views.author_form, name='update_form'),
    path('del/<int:id>', views.delete_author, name='delete_form'),
]