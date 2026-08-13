from django.urls import path

from shop import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('order/<int:pk>/', views.order_product, name="create_order"),
    path('order/success/', views.success, name="order_success")
]