from django.db import models
from django.contrib.auth.models import User

class todoo(models.Model):
    srno=models.AutoField(primary_key=True,auto_created=True)
    tital=models.CharField(max_length=40)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    
