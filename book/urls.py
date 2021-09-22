from django.urls import path, include

import author.views
import order.views
import authentication.views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book', views.BookView)
router.register('author', author.views.AuthorView)
router.register('user', authentication.views.CustomUserView)
router.register('order', order.views.OrderView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', views.show_all_books, name='index'),
    path('form/', views.book_form, name='book_form'),
    path('del/<int:id>/', views.deleted_form, name='deleted_form'),
    path('form/<int:id>/', views.book_form, name='updated_form'),
    path('ordered/', views.show_ordered_books, name='book_ordered'),
    path('<int:book_id>/', views.show_book_by_id, name='book_by_id'),
    path('sort/<str:field_name>/<str:state_sort>/', views.book_order, name='book_sort'),
    path('filter/<str:field_prop>/<str:field_value>/', views.show_book_by_field, name='book_search'),
    path('author/<int:author_id>/', views.show_book_by_author, name='book_by_author'),
    path('start/', views.start, name='start'),
]