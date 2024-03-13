from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("add-cell", views.CellCreateView.as_view(), name="add_cell"),
    path("<int:pk>/cell-detail", views.CellDetailView.as_view(), name="cell_detail"),
    # endpoint for getting the cell visualization template that will be embedded on the cell-detail page through JS 
    path("cell-visualization", views.cellVisualization)
]