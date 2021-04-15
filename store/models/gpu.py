from django.db import models

class GPU(models.Model):
    name = models.CharField(max_length=20)
    #this function returns the name table elements in str format
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_gpus():
        return GPU.objects.all()