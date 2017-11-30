from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class dateRequestForm(forms.ModelForm):
    interest_type = forms.ModelDate()
    class Meta:
        model = UserProfile
        fields = ('Date Details',)