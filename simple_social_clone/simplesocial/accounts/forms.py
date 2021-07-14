from django.contrib.auth import get_user_model
# this returns user model currently active in project
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    # ensure that they both don't have the exact same name

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
