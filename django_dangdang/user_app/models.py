from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    user_status = models.IntegerField()
    salt = models.CharField(max_length=40)

    class Meta:
        db_table = 't_user'