from django.forms import ModelForm
from .models import CustomUser


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
<<<<<<< HEAD
<<<<<<< HEAD
        fields = {'first_name', 'middle_name', 'last_name', 'email', 'password', 'role'}
=======
        fields = {'first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active'}
>>>>>>> 119b1d6 (add[User]: base url in main settings, output list of users)
=======
        fields = {'first_name', 'middle_name', 'last_name', 'email', 'password', 'role'}
>>>>>>> 4d977ed (add[User]: a form for creating user, methods, templates, urls, etc.)
