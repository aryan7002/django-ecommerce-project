from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.processor import Processor
from .models.harddisk import HardDisk
from .models.gpu import GPU
from .models.storage import Storage
from .models.ram import RAM
from .models.display import Display

# this class resolves the error of object_product(1) like and you can see proper name 
# and i have also added price and category will be shown  
class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']
class AdminCategory(admin.ModelAdmin):
    list_display=['name']
class AdminProcessor(admin.ModelAdmin):
    list_display=['name']
class AdminHardDisk(admin.ModelAdmin):
    list_display=['name']
class AdminGPU(admin.ModelAdmin):
    list_display=['name']
class AdminStorage(admin.ModelAdmin):
    list_display=['name']
class AdminRAM(admin.ModelAdmin):
    list_display=['name']
class AdminDisplay(admin.ModelAdmin):
    list_display=['inch']

# Register your models here.


admin.site.register(Product ,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Processor ,AdminProcessor)
admin.site.register(HardDisk ,AdminHardDisk)
admin.site.register(GPU ,AdminGPU)
admin.site.register(Storage ,AdminStorage)
admin.site.register(RAM,AdminRAM)
admin.site.register(Display,AdminDisplay)



