from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, CharField
from django.forms.widgets import TextInput


class UserLoginForm(Form):
    username = CharField(widget=TextInput(attrs={
            "class": "bg-light",
            "placeholder": "Username",
        })
    )
    password = CharField(widget=TextInput(attrs={
            "type": "password",
            "class": "bg-light",
            "placeholder": "Password",
        })
    )

class UserRegistrationForm(ModelForm):
    password = CharField(widget=TextInput(attrs={
            "type": "password",
            "class": "bg-light",
            "autocomplete": "new-password",
            "placeholder": "Password",
        })
    )
    password2 = CharField(widget=TextInput(attrs={
            "type": "password",
            "class": "bg-light",
            "autocomplete": "new-password",
            "placeholder": "Repeat password"
            })
    )
    
    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            "username": TextInput(attrs={
                "class": "bg-light",
                "placeholder": "Username",
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords don\'t match.')
        return cd['password2']