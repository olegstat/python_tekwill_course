from django.forms import ModelForm
from job_list.models import JobPost

class JobPostForm(ModelForm):
    class Meta:
        fields = ('title', 'job_description', 'due_date')
        model = JobPost