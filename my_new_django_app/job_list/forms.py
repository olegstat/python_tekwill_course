from django.forms import ModelForm, ValidationError
from job_list.models import JobPost
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JobPostForm(ModelForm):
    def clean_title(self):
        if len(self.cleaned_data['title']) < 5:
            raise ValidationError('Title could not be shorter that 5 characters!')
        return self.cleaned_data['title']
    class Meta:
        fields = ('title', 'job_description', 'due_date')
        model = JobPost

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')