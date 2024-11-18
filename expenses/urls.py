from django.urls import path

from .views import HomeView, ExpensesListView

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("expenses", ExpensesListView.as_view(), name="expenses")
]