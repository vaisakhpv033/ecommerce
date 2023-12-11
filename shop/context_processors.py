# Import the Category model from the current package
from .models import Category


# Define a function named 'menu_link' that takes a 'request' parameter
def menu_link(request):

    # retrieves all objects (categories) from the Category model in the database.
    links = Category.objects.all()

    # Return a dictionary containing the retrieved Category objects with the key 'links'
    return dict(links=links)
