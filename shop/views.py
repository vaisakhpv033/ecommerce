# Import necessary functions from Django
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Import models (Product and Category) from the current package
from .models import Product, Category


# Define a view function named 'allProdCat' that takes a request and an optional category slug as parameters
def allProdCat(request, c_slug=None):
    # Initialize variables for category page and products
    c_page = None  # This will store the category page (default value is None)
    products_list = None  # This will store the products associated with the category (default value is None)

    # Check if a category slug is provided
    if c_slug != None:
        # Get the category object from the database based on the provided slug
        c_page = get_object_or_404(Category, slug=c_slug)

        # Get all products objects associated with the category that are marked available
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        # If no category slug is provided, get all available products
        products_list = Product.objects.all().filter(available=True)

    # Create a Paginator object with 6 products per page
    paginator = Paginator(products_list, 6)

    try:
        # Attempt to get the 'page' parameter from the request's GET parameters
        page = int(request.GET.get('page', '1'))
    except ValueError:
        # If there's an error converting the 'page' parameter to an integer, default to page 1
        page = 1

    try:
        # Get the specified page of products from the Paginator
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        # If the requested page is empty or invalid, default to the last page
        products = paginator.page(paginator.num_pages)

    # Render the 'category.html' template with the category and products as context
    return render(request, "category.html", {'category': c_page, 'products': products})


def prodDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
