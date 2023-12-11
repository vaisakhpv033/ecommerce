from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


# Create your views here.
def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))

        if not products.exists():
            # Handle the case when no products are found
            return render(request, 'search.html', {'query': query, 'no_results': True})

    return render(request, 'search.html', {'query': query, 'products': products})
