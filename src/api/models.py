from django.db import models

# Create your models here.
class Tast(models.Model):
    title = models.CharField(max_length=200)
    complated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
