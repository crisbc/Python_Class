from django.shortcuts import render, redirect
from .forms import editUserInfoForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .models import Interests
from .forms import InterestsForm, UserForm
# Create your views here.
# @login required doesnt allow user to access particular view if not authenticated


@login_required
def index(request):
   # posts = Interests.objects.all()
    args = {'user': request.user}
    return render(request, 'userProfiles/UserProfiles.html',args)# , {'posts': posts}

@login_required
def other_users(request, pk=None):
   # form = InterestsForm()
    users = User.objects.exclude(id=request.user.id)
    if pk:
       user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'users': users}
    return render(request, 'userProfiles/otherUsers.html', args)


def user_questionnaire(request):
    try: profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/userProfiles')
    else:
        form = UserForm(instance=profile)
        args = {'form': form}
        return render(request, 'userProfiles/questionnaire.html', args)


# This view is for Interests form
@login_required
def post_new(request):
    try: profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = InterestsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/userProfiles')
    else:
        form = InterestsForm(instance=profile)
        args = {'form': form}
        return render(request, 'userProfiles/interestsModal.html', args)


@login_required
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

@login_required
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

