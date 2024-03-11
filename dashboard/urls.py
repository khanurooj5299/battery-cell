from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("add-cell", views.add_cell, name="add_cell"),
    path("<int:cell_id>/cell-info", views.cell_info)
]