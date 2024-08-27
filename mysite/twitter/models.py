from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    text = models.CharField(max_length=280)
    pub_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)