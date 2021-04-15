from django.db import models

class Processor(models.Model):
    name = models.CharField(max_length=20)
    #this function returns the name table elements in str format
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_processors():
        return Processor.objects.all()