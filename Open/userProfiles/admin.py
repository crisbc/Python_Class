from django.contrib import admin
from .models import Interests
from .models import UserProfile
# Register your models here.

# These are to view in admin


class UserProfileAdmin(admin.ModelAdmin):
    pass


class InterestsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interests)
admin.site.register(UserProfile)
