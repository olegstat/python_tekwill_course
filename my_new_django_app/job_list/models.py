from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    job_description = models.TextField()
    date = models.DateField(auto_now=True)
    due_date = models.DateField(auto_now=False)
    def __str__(self):
        return self.title
