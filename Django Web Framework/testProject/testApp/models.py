from django.db import models

# Create your models here.

#class Menu(models.Model):
#    name = models.CharField(max_length=100)
#    cuisine = models.CharField(max_length=100)
#    price = models.IntegerField()

### Creating a one-to-many relation

#class MenuCategory(models.Model):
#    menu_category_name = models.CharField(max_length = 200)

#class Menu(models.Model):
#    menu_item = models.CharField(max_length = 200, default = None)
#    price = models.IntegerField(null = False)
#    category_id = models.ForeignKey(MenuCategory, on_delete = models.PROTECT, default = None, related_name = "category_name")  

class Reservations(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    contact = models.CharField('Phone number',max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.name