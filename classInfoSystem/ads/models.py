from django.db import models

# Create your models here.

class Ads(models.Model):
    ads_name = models.CharField(max_length = 50)
    dep_name =models.ManyToManyField("department.Department")
    image_ads = models.FileField(upload_to='image',blank=True)
    def __str__(self):
       return self.ads_name
