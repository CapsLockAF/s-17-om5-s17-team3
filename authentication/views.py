from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import UserForm

num_items = 5


def all_users(request):

    users = CustomUser.get_all()
    paginator = Paginator(users, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, 'authentication/user_list.html',
                  {
                    'title': "Library Users",
                    'heading': "List of all Users",
                    "page_obj": page_obj,
                    "page_nums": page_nums,
                   }
                  )


def view_user(request, id=0):
    user_by_id = CustomUser.get_by_id(id)
    return render(request, 'authentication/user_view.html',
                  {
                      'title': "User by id",
                      'heading': "User Information",
                      "user_by_id": user_by_id,
                  })


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            user = CustomUser.get_by_id(id)
            form = UserForm(instance=user)
        return render(request, 'authentication/user_form.html', {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.objects.get(id=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():

            form.save()
        else:
            return render(request, 'authentication/user_form_error.html')
        return redirect('users')


def delete_user(request, id=0):
    user = CustomUser.objects.get(id=id)
    user.delete()
    users = CustomUser.get_all()
    paginator = Paginator(users, num_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_nums = range(page_obj.paginator.num_pages)
    return render(request, 'authentication/user_list.html',
                  {
                      'title': "Library Users",
                      'heading': "List of all Users",
                      "page_obj": page_obj,
                       "page_nums": page_nums,
                  })