from django.db import models

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Delivered', 'Delivered'),
]

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    item_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_date = models.DateField()
    delivery_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.item_description}"

    def payment_status(self):
        payment = getattr(self, 'payment', None)
        if payment and payment.paid:
            return 'Paid'
        return 'Unpaid'

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.order.customer_name} - {self.amount}"
