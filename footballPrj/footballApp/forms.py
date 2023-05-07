from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Game
from django.forms import ModelForm, TextInput


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['firstTeam', 'firstTeamStatus', 'goalsFirstTeam', 'playersFirstTeam',
                  'secondTeam', 'secondTeamStatus', 'goalsSecondTeam', 'playersSecondTeam',
                  'eventOwner', 'eventStatus']
        widgets = {
            'firstTeam': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First team',
            }),
            'firstTeamStatus': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'win/loss',
            }),
            'goalsFirstTeam': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'score',
            }),
            'playersFirstTeam': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'players',
            }),
            'secondTeam': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Second team',
            }),
            'secondTeamStatus': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'win/loss',
            }),
            'goalsSecondTeam': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'score',
            }),
            'playersSecondTeam': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'players',
            }),
            'eventOwner': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'user name',
            }),
            'eventStatus': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'status',
            }),
        }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control mb-3',
    }))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3'
    }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3'
    }))

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
