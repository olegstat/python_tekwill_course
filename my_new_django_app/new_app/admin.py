from django.contrib import admin
from new_app.models import BlogPost, Author
from questions.models import Question, Choice, QuestionAnswer

admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuestionAnswer)