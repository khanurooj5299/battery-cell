from django.shortcuts import render

#view for main dashboard of a user
def index(request):
    return render(request, 'dashboard/index.html')

#view for info of a particular cell
def cell_info(request, cell_id):
    return render(request, 'dashboard/cell_info.html')

def add_cell(request):
    return render(request, 'dashboard/add_cell.html')