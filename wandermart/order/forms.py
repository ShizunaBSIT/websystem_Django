from django import forms
from .models import Order
from product_post.models import Product

class OrderForm(forms.ModelForm):

    quantity = forms.IntegerField(min_value=1, initial=1)

    class Meta:
        model = Order
        fields = ['quantity', 'address', 'phoneContact']
        widgets = {'qantity': forms.NumberInput(attrs={'class':'form-control'})}

