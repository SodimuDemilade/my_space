from django.contrib import admin
from . import models

# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
    # this is done because group is the parent model of groupmember and we want to be able to edit it in the admin page

admin.site.register(models.Group)
