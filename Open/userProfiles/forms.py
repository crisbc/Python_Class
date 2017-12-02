from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Interests, UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_location', 'user_birthday', 'user_gender',)


class InterestsForm(forms.ModelForm):
    interest_type = forms.ModelMultipleChoiceField(queryset=Interests.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = UserProfile
        fields = ('interest_type',)


class editUserInfoForm(UserChangeForm):

    class Meta:
        model = User
        fields= (
            'email',
            'first_name',
            'last_name',
            'password',

        )


