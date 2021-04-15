from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    #this function returns the name table elements in str format
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()