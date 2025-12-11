from django import forms
from .models import Order, Payment

class OrderForm(forms.ModelForm):
    order_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    delivery_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'item_description', 'status', 'order_date', 'delivery_date']

class PaymentForm(forms.ModelForm):
    payment_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'paid', 'payment_date']
