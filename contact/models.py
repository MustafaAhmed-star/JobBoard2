from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length = 50)
    phone_num = models.CharField(max_length = 20)
    email = models.EmailField(max_length=100)
    
    
    
    def __str__(self) -> str:
        return self.email
  