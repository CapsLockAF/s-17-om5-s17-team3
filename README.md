## Django

`python manage.py runserver`
## Main
```python
urlpatterns = [
    path('', include('book.urls')),
    path('author/', include('author.urls')),
    path('user/', include('authentication.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
]
```
### Books
```python
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
]
```
### User
```python
urlpatterns = [
    path('', views.all_users, name='users'),
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
]
```
### Order
```python
urlpatterns = [
    path('', views.all_users, name='users'),
    path('<int:id>/', views.view_user, name='view_user'),
    path('form/<int:id>/', views.user_form, name='user_form'),
    path('form/<int:id>/delete/', views.delete_user, name='delete_form'),
]
```
### Author
```python
urlpatterns = [
    path('', views.all_authors, name='authors'),
    path('form/', views.author_form, name='author_form'),
    path('form/<int:id>', views.author_form, name='update_form'),
    path('del/<int:id>', views.delete_author, name='delete_author'),
]
```