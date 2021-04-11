from django.db import models
from .category import Category
from .processor import Processor
from .harddisk import HardDisk
from .storage import Storage
from .ram import RAM
from .gpu import GPU
from .display import Display

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category =models.ForeignKey(Category , on_delete=models.CASCADE ,default=0)
    display = models.ForeignKey(Display,on_delete= models.CASCADE,default=0)
    processor = models.ForeignKey(Processor,on_delete= models.CASCADE,default=0)
    harddisk = models.ForeignKey(HardDisk,on_delete=models.CASCADE,default=0)
    storage= models.ForeignKey(Storage,on_delete=models.CASCADE,default=0)
    ram = models.ForeignKey(RAM,on_delete=models.CASCADE,default=0)
    gpu = models.ForeignKey(GPU,on_delete=models.CASCADE,default=0)
    description = models.CharField(max_length=200,default='')
    image= models.ImageField(upload_to='uploads/products/')
