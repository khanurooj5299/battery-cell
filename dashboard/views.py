from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.views.generic.list import ListView
from .forms import CellCreateForm
from .models import BatteryCell

#view for main dashboard of a user
class DashboardView(ListView):
    model = BatteryCell
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'cell_list'
    
    # show only those items which were added by the logged in user
    def get_queryset(self):
        authenticated_user = self.request.user
        queryset = BatteryCell.objects.filter(created_by=authenticated_user)
        return queryset

#view for info of a particular cell
def cell_info(request, cell_id):
    return render(request, 'dashboard/cell_info.html')

class CellCreateView(CreateView):
    form_class = CellCreateForm
    template_name = "dashboard/add_cell.html"
    success_url = "/dashboard"
    
    # overriding to insert the user_id field for a cell
    def form_valid(self, form):
        # image_data_url key is added to the form through JS on frontend
        form.instance.image_data_url = self.request.POST['image_data_url']
        # adding user_id
        form.instance.created_by = self.request.user
        print(self.request.user)
        return super().form_valid(form)
    