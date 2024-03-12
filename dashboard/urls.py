from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("add-cell", views.CellCreateView.as_view(), name="add_cell"),
    path("<int:cell_id>/cell-info", views.cell_info)
]