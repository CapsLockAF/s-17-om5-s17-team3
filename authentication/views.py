from django.shortcuts import render, redirect
from .models import *
from .forms import UserForm
from django.core.exceptions import ObjectDoesNotExist


def all_users(request):
    users = CustomUser.get_all()
    return render(request, 'authentication/user_list.html',
                  {
                    'title': "Library Users",
                    'heading': "List of all Users",
                    "users": users,
                   }
                  )
