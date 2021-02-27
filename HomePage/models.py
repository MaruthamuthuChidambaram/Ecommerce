from django.db import models

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)