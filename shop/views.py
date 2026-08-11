from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from shop.models import Product


# Create your views here.
def get_home(request):
    return render(request, 'shop/home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = 'pk'
