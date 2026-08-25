from django.contrib import admin
from . models import Product

class ProductAdmim(admin.ModelAdmin):
    list_display=("product_title",'product_price','product_description','is_active','available_qty','product_img_url')
admin.site.register(Product ,ProductAdmim)
# Register your models here.


