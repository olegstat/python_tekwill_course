from django.contrib import admin
from questions.models import Question, Choice, QuestionAnswer

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuestionAnswer)
