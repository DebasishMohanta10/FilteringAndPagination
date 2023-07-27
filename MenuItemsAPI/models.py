from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    inventory = models.IntegerField()
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=1,related_name='menuitems')

    class Meta:
        verbose_name_plural = "MenuItems"
    
    def __str__(self):
        return self.name
