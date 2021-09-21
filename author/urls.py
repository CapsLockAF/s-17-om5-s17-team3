from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', views.AuthorView)

urlpatterns = [
    path('', views.all_authors, name='authors'),
    path('form/', views.author_form, name='author_form'),
    path('form/<int:id>', views.author_form, name='update_form'),
    path('del/<int:id>', views.delete_author, name='delete_author'),
]