from django.contrib import admin
from .models import Product, Review
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'review_text', 'rating', 'is_reviewed', 'created_at', 'updated_at')
    list_filter = ('is_reviewed', 'product')
    search_fields = ('author_name', 'review_text')

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)