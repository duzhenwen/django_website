from django import forms
from .models import user_infor

class registerForm(forms.Form):
    class Meta:
        model=user_infor
        fields=('username','telephone','email','password')
