from django.db import models


class Products(models.Model):
    ProductName = models.CharField(max_length=50,primary_key=True)
    Description = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='Product Images',blank=True)

