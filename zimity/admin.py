from zimity.models import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

admin.site.register(Imprint)
#admin.site.register(Comment)
#admin.site.register(Message)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
    
admin.site.register(User, UserProfileAdmin)