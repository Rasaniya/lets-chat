from django.db import models

# Create your models here.
class Text(models.Model):
    name= models.CharField(max_length=25)
    message = models.TextField(max_length=555)

    def __str__ (self):
        return "Message by: " + self.name