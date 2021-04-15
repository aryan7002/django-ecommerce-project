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
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image= models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();
    @staticmethod
    def get_all_products_by_processorID(processor_id):
        if processor_id:
            return Product.objects.filter(processor = processor_id)
        else:
            return Product.get_all_products();
    
    @staticmethod
    def get_all_products_by_gpuID(gpu_id):
        if gpu_id:
            return Product.objects.filter(gpu = gpu_id)
        else:
            return Product.get_all_products();
    