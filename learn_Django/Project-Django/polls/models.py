from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.
class Question(models.Model):
    question_text = models.CharField('Question Title',max_length = 255)
    pub_date = models.DateTimeField('date published')
   
    def __str__(self):
        return self.question_text 
    
    @admin.display(
          boolean=True,
          ordering='pub_date',
          description='Published Recently?'
    )
   
    def was_published_recently(self):
        #Check pub_date is within the last day (around 24 hours)
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 255)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
