# Import necessary module for creating Django database models
from django.db import models
from django.urls import reverse


# Create a new model named 'Category'
class Category(models.Model):
    # Field to store the name of the category, limited to 250 characters, and must be unique
    name = models.CharField(max_length=250, unique=True)

    # Field for a 'slug,' a simplified version of the name used in URLs, also limited to 250 characters and must be
    # unique
    slug = models.SlugField(max_length=250, unique=True)

    # Field to store a description of the category, allowing it to be empty
    description = models.TextField(blank=True)

    # Field to store an image related to the category, with the option for it to be empty, stored in the 'category'
    # directory
    image = models.ImageField(upload_to='category', blank=True)

    # Meta information about the model
    class Meta:
        # Specify the default ordering for queries to be based on the 'name' field
        ordering = ('name',)

        # Set a user-friendly name for a single instance of the model in the Django admin interface
        verbose_name = 'category'

        # Set a user-friendly plural name for multiple instances of the model in the Django admin interface
        verbose_name_plural = 'categories'

    # Method to get the URL for a category
    def get_url(self):
        # Use the reverse function to generate a URL for the 'shop:products_by_category' view
        # The URL is constructed based on the 'slug' attribute of the current Category instance
        return reverse('shop:products_by_category', args=[self.slug])

    # Method to represent the model instance as a human-readable string, returning the category name
    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    # Field to store the price of the product, represented as a decimal with up to 10 digits and 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Field for a foreign key relationship with the Category model, specifying that if a related category is deleted,
    # also delete the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product', blank=True)

    # Field to store the stock quantity of the product
    stock = models.IntegerField()

    # Field to indicate whether the product is currently available, with a default value of True
    available = models.BooleanField(default=True)

    # Field to store the date and time when the product was created, automatically set to the current date and time
    # when the object is created
    created = models.DateTimeField(auto_now_add=True)

    # Field to store the date and time when the product was last updated, automatically set to the current date and
    # time when the object is updated
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:prodCatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
