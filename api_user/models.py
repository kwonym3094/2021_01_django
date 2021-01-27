from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "User"