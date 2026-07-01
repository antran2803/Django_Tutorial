from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField(max_length=100 , blank=False, null=False)
    fullname = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.fullname
    class Meta:
     verbose_name = "subscriber"
     verbose_name_plural = "subscribers"