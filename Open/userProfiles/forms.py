from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Interests, UserProfile, GenderPreference


class UserForm(forms.ModelForm):
    user_gender_pref = forms.ModelMultipleChoiceField(queryset=GenderPreference.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = UserProfile
        fields = ('user_location', 'user_birthday', 'user_gender','user_gender_pref', 'partner_location_preference')


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


