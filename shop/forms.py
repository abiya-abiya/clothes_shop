from django import forms


from shop.models import Order


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'phone',
            'address',
            'quantity',
        ]
    def save(self, commit: bool = True):
        customer_name = self.cleaned_data.get("customer_name")

        phone = self.cleaned_data.get("phone")
        address = self.cleaned_data.get("address")
        quantity = self.cleaned_data.get("quantity")
        return Order.objects.create(
            customer_name=customer_name,
            phone=phone,
            address=address,
            quantity=quantity
        )