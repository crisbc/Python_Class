from directmessages.apps import Inbox
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from requests.models import Request

# Create your views here.
@login_required
def index(request, pk=None):
    users = User.objects.exclude(id=request.user.id)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'users': users}
    return render(request, 'Messages/Inbox.html', args)
@login_required
def send_message(from_user,to_user,message):
    Inbox.send_message(from_user,to_user,message)
@login_required
def get_unread(user):
    Inbox.get_unread(user)
@login_required
def read_message(message):
    Inbox.read_message(message)
@login_required
def get_conversation(user1, user2,_limit_,_reversed_,_mark_read_):
    Inbox.get_conversation(user1,user2,_limit_,_reversed_,_mark_read_)
