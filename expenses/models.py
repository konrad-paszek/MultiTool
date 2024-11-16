from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('RENT', 'Rent/Mortgage'),
        ('UTIL', 'Utilities'),
        ('FOOD', 'Groceries/Food'),
        ('TRANS', 'Transportation'),
        ('MED', 'Medical/Healthcare'),
        ('INS', 'Insurance'),
        ('ENT', 'Entertainment'),
        ('EDU', 'Education'),
        ('SAV', 'Savings/Investment'),
        ('OTH', 'Other Expenses'),
    )
    title = models.CharField(max_length=30)
    expected_cost = models.DecimalField(max_digits=8, decimal_places=2)
    real_cost = models.DecimalField(max_digits=8, decimal_places=2)
    deadline = models.DateField()
    pay_date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

