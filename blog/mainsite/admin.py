from django.contrib import admin
from .models import Post
from .models import NewTable
from .models import Product
from .models import Maker
from .models import ProductModel
from .models import PhoneProduct
from .models import ProductPhoto

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'slug',
                    'created_date', 'published_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_model', 'name', 'year', 'price')
    search_fields = ('name',)
    ordering = ('-price',)

admin.site.register(Post, PostAdmin)
admin.site.register(PhoneProduct, ProductAdmin)

admin.site.register(NewTable)
admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(ProductModel)
admin.site.register(ProductPhoto)
