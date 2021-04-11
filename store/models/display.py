from django.db import models

class Display(models.Model):
    inch = models.FloatField(max_length=20)
    #this function returns the name table elements in str format
    def __str__(self):
        return str(self.inch)