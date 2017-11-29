from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    # posts = Interests.objects.all()
    args = {'user': request.user}
    return render(request, 'requests/requests.html', args)# , {'posts': posts}
