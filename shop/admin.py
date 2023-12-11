# Import necessary module for Django admin interface
from django.contrib import admin

# Import models (Category and Product) from the current package
from .models import Category, Product


# Register your models with the Django admin
class CategoryAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the list view of the admin interface for Category
    list_display = ['name', 'slug']

    # Specify that the 'slug' field should be automatically populated based on the 'name' field
    prepopulated_fields = {'slug': ('name',)}


# Register the Category model with the custom admin interface
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the list view of the admin interface for Product
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']

    # Specify that certain fields ('price', 'stock', 'available') can be edited directly in the list view
    list_editable = ['price', 'stock', 'available']

    # Specify that the 'slug' field should be automatically populated based on the 'name' field
    prepopulated_fields = {'slug': ('name',)}

    # Specify the number of items to display per page in the admin interface
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
