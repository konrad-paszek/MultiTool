from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)
