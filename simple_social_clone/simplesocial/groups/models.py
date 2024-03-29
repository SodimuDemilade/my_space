from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# slugify allows us to remove any characters that are not alphanumeric or hyphens or underscores
import misaka
# for marked down texts
from django.contrib.auth import get_user_model
User = get_user_model()
# this allows us to call things off of the current user session
from django import template
register = template.Library()
# this is how we can use custom template tags

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug =slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse ('groups:single',kwargs={'slug':self.slug})

    class Meta():
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    # user_groups allows us to do a link from the post to the groupmemeber

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group', 'user')
