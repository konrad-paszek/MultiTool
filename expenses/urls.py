from django.urls import path

from .views import HomeView, ExpensesListView, DraftListView

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("expenses/", ExpensesListView.as_view(), name="expenses"),
    path("drafts/", DraftListView.as_view(), name="drafts"),
]