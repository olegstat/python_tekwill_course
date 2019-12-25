from django.db import models

class Question(models.Model):
    text = models.TextField()
    publication_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.TextField()
    def __str__(self):
        return self.choice_text

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return (f"{self.question}: {self.choice}")
    
