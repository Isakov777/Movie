from email.policy import default
from allauth.account.forms import SignupForm
from django import forms

class UserSingUpForm(SignupForm):
    age = forms.IntegerField()
    profile = forms.ImageField(required=False,   )
 
    def save(self, request):
        user = super(UserSingUpForm, self).save(request)
        user.age = self.cleaned_data['age']
        user.profile = self.cleaned_data['profile']
        user.save()
        return user



    