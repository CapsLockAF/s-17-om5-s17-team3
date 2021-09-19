from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_books, name='index'),
    path('form/', views.book_form, name='book_form'),
    path('del/<int:id>', views.deleted_form, name='deleted_form'),
    path('form/<int:id>', views.book_form, name='updated_form'),
    path('ordered/', views.show_ordered_books, name='book'),
    path('<int:book_id>/', views.show_book_by_id, name='book'),
    path('sort/<str:field_name>/<str:state_sort>/', views.book_order, name='book'),
    path('filter/<str:field_prop>/<str:field_value>', views.show_book_by_field, name='book'),
    path('author/<int:author_id>/', views.show_book_by_author, name='book'),
    path('start/', views.start, name='index'),
]