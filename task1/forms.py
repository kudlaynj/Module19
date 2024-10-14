from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите логин',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(min_length=8,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 }))
    repeat_password = forms.CharField(min_length=8,
                                      required=True,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль',
                                                                        'class': 'form-control',
                                                                        'data-toggle': 'password',
                                                                        'id': 'password',
                                                                        }))

    age = forms.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)],
                             label="Введите свой возраст")
