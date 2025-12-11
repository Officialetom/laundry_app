from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Payment
from .forms import OrderForm, PaymentForm

def home(request):
    orders = Order.objects.all()
    # Dashboard stats
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    in_progress = orders.filter(status='In Progress').count()
    completed = orders.filter(status='Completed').count()
    delivered = orders.filter(status='Delivered').count()
    total_paid = Payment.objects.filter(paid=True).count()
    total_unpaid = Payment.objects.filter(paid=False).count()
    
    context = {
        'orders': orders,
        'total_orders': total_orders,
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed,
        'delivered': delivered,
        'total_paid': total_paid,
        'total_unpaid': total_unpaid
    }
    return render(request, 'laundry_app/home.html', context)

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'laundry_app/form.html', {'form': form, 'title': 'Add Order'})

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm(instance=order)
    return render(request, 'laundry_app/form.html', {'form': form, 'title': 'Edit Order'})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('home')

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaymentForm()
    return render(request, 'laundry_app/form.html', {'form': form, 'title': 'Add Payment'})
