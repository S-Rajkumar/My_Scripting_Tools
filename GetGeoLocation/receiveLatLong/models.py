from django.db import models

# Create your models here.
class LogSystem(models.Model) :

    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length = 50, default="127.0.0.1")
    lat = models.CharField(max_length = 50, default="0")
    long = models.CharField(max_length = 50, default="0")
    user_agent = models.TextField(default="useragent")
    time = models.DateTimeField(auto_now_add = True)
