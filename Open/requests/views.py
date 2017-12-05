from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from requests.models import Request

# Create your views here.
@login_required
def index(request, pk=None):
    users = User.objects.exclude(id=request.user.id)
    try:
        dateRequest=Request.objects.get(current_user=request.user)
    except:
        Request.objects.create(current_user=request.user)
        dateRequest=Request.objects.get(current_user=request.user)
    friends=dateRequest.users.all()
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'users': users, 'friends': friends}
    return render(request, 'requests/requests.html', args)
@login_required
def sendRequest(request, operation, pk=None):
    friend=User.objects.get(pk=pk)
    if operation == 'add':
        Request.sendRequest(request.user, friend)
    elif operation == 'remove':
        Request.removeRequest(request.user, friend)
    return redirect('requests:index')
