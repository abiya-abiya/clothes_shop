
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from shop.models import Product, Category


# Create your views here.
def get_home(request):
    return render(request, 'shop/home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get("category")

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context



class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = 'pk'
