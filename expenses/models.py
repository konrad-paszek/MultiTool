import calendar

from django.db import models

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

class ExpenseDraftList(models.Model):
    name = models.CharField(max_length=255, default="Default Draft List", help_text="Name of the draft list", unique=True)

    def __str__(self):
        return self.name

class ExpenseDraft(models.Model):
    title = models.CharField(max_length=30)
    expected_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    pay_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    draft_list = models.ForeignKey(ExpenseDraftList, related_name='drafts', on_delete=models.CASCADE, help_text="The draft list this expense belongs to")


class ExpenseList(models.Model):
    month = models.IntegerField(choices=[(i, calendar.month_name[i]) for i in range(1, 13)], help_text="Month (e.g., January, February)")
    year = models.IntegerField(help_text="Year (e.g., 2024)")

    name = models.CharField(max_length=255, blank=True, editable=False, help_text="Generated automatically as 'Month Year'")


    def save(self, *args, **kwargs):
        self.name = f"{calendar.month_name[self.month]} {self.year}"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-year", "-month"]


class Expense(models.Model):
    title = models.CharField(max_length=30)
    expected_cost = models.DecimalField(max_digits=8, decimal_places=2)
    real_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    pay_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    expense_list = models.ForeignKey(ExpenseList, related_name='expenses', on_delete=models.CASCADE, help_text="The list this expense belongs to")

    def __str__(self):
        return f"{self.title} ({self.expense_list.name})"

