from django.db import models

# Create your models here.
class Client(models.Model):
    GENDER_CHOICES = [
        ('male' ,'Male'),
        ('female' ,'Female')
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(choices = GENDER_CHOICES , default= 'male' ,max_length=6)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(Client , on_delete = models.CASCADE , related_name = 'all_posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} by {self.author.name}"