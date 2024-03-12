from django import forms
from .models import BatteryCell

class CellCreateForm(forms.ModelForm):
    class Meta:
        model = BatteryCell
        exclude = ('created_by', 'cell_id', 'image_data_url')