from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.views.generic.edit import CreateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from barcode import Code128
from io import BytesIO
import base64
from barcode.writer import ImageWriter
from .forms import CellCreateForm
from .models import BatteryCell
from .visualization import getContext

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
class CellDetailView(DetailView):
    model = BatteryCell
    template_name = 'dashboard/cell_detail.html'
    context_object_name = 'cell'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #setting the barcode in context
        bytes = BytesIO()
        Code128(context['cell'].cell_id, writer=ImageWriter()).write(bytes)
        binary_data = bytes.getvalue()
        base64_encoded_string = base64.b64encode(binary_data).decode('utf-8')
        context["barcode"] = base64_encoded_string
        return context

#view for creating a cell
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
    
# endpoint for getting the cell visualization template that will be embedded on the cell-detail page through JS 
def cellVisualization(request):
    # expecting impedance data as csv file for creating the visualization template
    if(request.method != "POST"):
        return HttpResponseNotAllowed(['POST'])
    else:
        datasetFile = request.FILES['dataset']
        context = getContext(datasetFile)
        return render(request, "dashboard/cell_visualization_component.html", context)