from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Expense, ExpenseDraft, ExpenseDraftList


class HomeView(TemplateView):
    template_name = "base.html"

class ExpensesListView(ListView):
    template_name = "expenses/expenses.html"
    context_object_name = "expenses"

    def get_queryset(self):
        return Expense.objects.all()

class DraftListView(ListView):
    template_name = "expenses/drafts.html"
    context_object_name = "draft_lists"

    def get_queryset(self):
        return ExpenseDraftList.objects.all()

class DraftListCreateView(CreateView):
    model = ExpenseDraftList
    fields = ["name"]
    success_url = reverse_lazy('drafts')

class DraftListDetailView(DetailView):
    model = ExpenseDraftList
    fields = ["name"]
    template_name = "expenses/draft-detail.html"
    context_object_name = "draft_list"

class DraftUpdateView(ListView):
    model = ExpenseDraftList
    fields = ["name"]
    success_url = reverse_lazy('drafts')

    def get_queryset(self):
        return ExpenseDraftList.objects.all()

class DraftDeleteView(DeleteView):
    model = ExpenseDraftList
    success_url = "/drafts"