from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CellCreateForm

#view for main dashboard of a user
def index(request):
    return render(request, 'dashboard/index.html')

#view for info of a particular cell
def cell_info(request, cell_id):
    return render(request, 'dashboard/cell_info.html')

class CellCreateView(CreateView):
    form_class = CellCreateForm
    context_object_name = "cell"
    template_name = "dashboard/add_cell.html"
    success_url = "dashboard"
    
    # overriding to insert the user_id field for a cell
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    