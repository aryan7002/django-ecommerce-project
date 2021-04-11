from django.db import models

class Storage(models.Model):
    name = models.SlugField(max_length=20)
    #this function returns the name table elements in str format
    def __str__(self):
        return self.name