from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

#from .models import Interests


#class InterestsForm(forms.ModelForm):
 #   Interests = forms.ModelMultipleChoiceField(queryset=Interests.objects.all(), widget=forms.CheckboxSelectMultiple())

  #  class Meta:
   #     model = Interests
    #    fields = ('userInterests',)

class editUserInfoForm(UserChangeForm):

    class Meta:
        model = User
        fields= (
            'email',
            'first_name',
            'last_name',
            'password',

        )


