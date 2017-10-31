from django.db import models

# Create your models here.


class Locator(models.Model):
    created = models.DateTimeField(auto_now_add= True, primary_key=True)
    latitude = models.CharField(max_length= 100)
    longitude = models.CharField(max_length= 100)
    scu_id = models.CharField(max_length=100)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return str(self.created)
