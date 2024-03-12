from django.shortcuts import render
from django.views.generic.edit import CreateView
from dashboard.models import BatteryCell

#view for main dashboard of a user
def index(request):
    return render(request, 'dashboard/index.html')

#view for info of a particular cell
def cell_info(request, cell_id):
    return render(request, 'dashboard/cell_info.html')

class CellCreateView(CreateView):
    model = BatteryCell
    context_object_name = "cell"
    