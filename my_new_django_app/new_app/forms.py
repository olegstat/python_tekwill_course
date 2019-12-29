from django.forms import ModelForm, ValidationError
from new_app.models import BlogPost

class BlogPostForm(ModelForm):

    def clean_title(self):
        if "web" in self.cleaned_data['title'].lower():
            raise ValidationError('Title could not be shorter than 5 characters!')
        return self.cleaned_data['title']
        
    class Meta:
        fields = ('title', 'content', 'author')
        model = BlogPost