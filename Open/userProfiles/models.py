from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    interest_type = models.ManyToManyField('Interests', blank=True)
    user_location = models.CharField(max_length=250,default='Any', editable=True)
    FEMALE = 'FM'
    MALE = 'ML'
    USER_Gender_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    user_gender = models.CharField(
        max_length=2,
        choices=USER_Gender_CHOICES,
        default=MALE,
    )
    user_birthday = models.DateField(blank=True, null=True)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)



class Interests(models.Model):
    #user_details = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    userInterests = models.CharField(max_length=250)
    chosen_Interests = models.BooleanField(default=False)
    # def_str returns the names of items in database

    def __str__(self):
        return self.userInterests
