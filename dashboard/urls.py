from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:cell_id>/cell-info", views.cell_info)
]