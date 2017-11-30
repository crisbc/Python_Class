from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .forms import 

# Create your views here.
@login_required
def index(request):
    args = {'user': request.user}
    return render(request, 'requests/requests.html', args)
@login_required
def sendRequest(request):
    args = {'user': request.user}
    return render(request, 'requests/sendRequest.html', args)
@login_required
def profilePreview(request):
    args= {'user': request.user}
    return render(request, 'requests/profilePreview.html', args)