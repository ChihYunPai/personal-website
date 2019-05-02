from django.contrib import admin
from .models import Post
from .models import NewTable
from .models import Product

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'slug',
                    'created_date', 'published_date')

admin.site.register(Post, PostAdmin)
admin.site.register(NewTable)
admin.site.register(Product)
