from django.forms import ModelForm
from .models import CustomUser


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = {'first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active'}