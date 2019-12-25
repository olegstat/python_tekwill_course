from django.forms import ModelForm
from new_app.models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        fields = ('title', 'content')
        model = BlogPost