from django.urls import path

from .views import HomeView, ExpensesListView, DraftListView, DraftListCreateView, DraftDeleteView, DraftUpdateView, DraftListDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("expenses/", ExpensesListView.as_view(), name="expenses"),
    path("drafts/", DraftListView.as_view(), name="drafts"),
    path("drafts-create/", DraftListCreateView.as_view(), name="add-draft-list"),
    path("drafts-delete/<int:pk>/", DraftDeleteView.as_view(), name="delete-draft-list"),
    path("drafts-update/<int:pk>/", DraftUpdateView.as_view(), name="edit-draft-list"),
    path("drafts-detail/<int:pk>/", DraftListDetailView.as_view(), name="draft-detail")
]