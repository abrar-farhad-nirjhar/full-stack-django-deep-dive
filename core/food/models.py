from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,  default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAQWqABN-gmjy8EvyamtBSOSUBQgjPndO1QqZTPVai&s")

    def __str__(self) -> str:
        return self.item_name
