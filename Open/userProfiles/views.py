from django.shortcuts import render, redirect
from .forms import editUserInfoForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from .models import Interests
# from .forms import InterestsForm
# Create your views here.


def index(request):
   # posts = Interests.objects.all()
    args = {'user': request.user}
    return render(request, 'userProfiles/UserProfiles.html',args)# , {'posts': posts}


def post_new(request):
   # form = InterestsForm()
    return render(request, 'userProfiles/interestsModal.html') # , {'form': form}


def edit_userinfo(request):
    if request.method == 'POST':
        form = editUserInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/userProfiles')
    else:
        form = editUserInfoForm(instance=request.user)
        args = {'form':form}
        return render(request, 'userProfiles/edit_userinfo.html',args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/userProfiles')
        else:
            return redirect('/userProfiles/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request,'userProfiles/change_password.html', args)

