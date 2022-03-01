from django.contrib import admin
from .models import Product, ProductImage



class InLineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InLineProductImage, ]


admin.site.register(Product, ProductAdminDisplay)
# admin.site.register(ProductImage)
