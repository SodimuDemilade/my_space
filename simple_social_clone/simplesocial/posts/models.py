from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
# connect curent post to user

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    # this allows the date to be automatically filled according to when the post is made
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})
        # we will use primary key as a way to link post back to url

    class Meta():
        ordering = ['-created_at']
        # '-' indicates we see them is descending order
        unique_together = ['user','message']
        # this way every message is uniquely linked to a user
