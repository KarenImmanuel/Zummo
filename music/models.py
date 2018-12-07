from django.db import models

# Create your models here.


class Categories(models.Model):
    categories_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.categories_text
    


class Product(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_text = models.CharField(max_length=200)
    price=models.FloatField(default=0.0)
    pict=models.CharField(max_length=1000,default='SOME STRING')
    filter1_age=models.CharField(max_length=100,default='SOME STRING')
    filter2_gender=models.CharField(max_length=100,default='SOME STRING')
    filter3_type=models.CharField(max_length=100,default='SOME STRING')

    def __str__(self):
        return self.product_text

    