from django.views.generic import TemplateView, ListView
from .models import Expense


class HomeView(TemplateView):
    template_name = "base.html"

class ExpensesListView(ListView):
    template_name = "expenses/expenses.html"
    context_object_name = "expenses"

    def get_queryset(self):
        return Expense.objects.all()