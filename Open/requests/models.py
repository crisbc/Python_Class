from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Treating Request1 as people you have added ie) requests from you
class Request(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User, related_name='owner', null=True)
    @classmethod
    def sendRequest(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)
    @classmethod
    def removeRequest(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
#Treating Request2 as people who have added you ie) requests to you
#class Request2(models.Model):
    #users=models.ManyToManyField(User)
    #current_user=models.ForeignKey(User, related_name='owner', null=True)
    #@classmethod
    #def receiveRequest(cls, current_user, new_friend):
        #friend, created = cls.objects.get_or_created(current_user=current_user)
        #friend.users.add(new_friend)
    #@classmethod
    #def declineRequest(cls, current_user, new_friend):
        #friend, created = cls.objects.get_or_created(current_user=current_user)
        #friend.users.remove(new_friend)