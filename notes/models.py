from django.db import models
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from colorfield.fields import ColorField
# Create your models here.
class Note(models.Model):
    
    COLOR_CHOICES = [
        ( "#E06C75" ,"RED" ),
        ("#E5C07B" ,"YELLOW"),
        ("#98C379" ,"GREEN"),
        ("#61AFEF" , "BLUE"),
        ("#ECECEC","DEFAULT"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=20,choices = COLOR_CHOICES,default="#ECECEC")
    # color = ColorField(max_length=20,choices = COLOR_CHOICES,default="#ECECEC")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title