from django.contrib import admin
from .models import Expense


from .models import ExpenseDraftList, ExpenseDraft, ExpenseList, Expense

@admin.register(ExpenseDraftList)
class ExpenseDraftListAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ExpenseDraft)
class ExpenseDraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'expected_cost', 'category', 'draft_list')


@admin.register(ExpenseList)
class ExpenseListAdmin(admin.ModelAdmin):
    list_display = ('name', 'month', 'year')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'expected_cost', 'real_cost', 'expense_list')