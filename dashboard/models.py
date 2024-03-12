from django.db import models
from django.contrib.auth.models import User

class BatteryCell(models.Model):
    # image is stored as a base64 encoded data url
    image_data_url = models.TextField()
    cell_id = models.CharField(max_length=10, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # META INFORMATION
    cell_condition = models.CharField(max_length=8, choices={'New':'New', 'Recycled': 'Recycled'}, default='Recycled')
    manufacturer = models.CharField(max_length=20, default='Molicel')
    model = models.CharField(max_length=30, default='INR21700-P45B')
    type = models.CharField(max_length=20, default='Li-ion')
    form_factor = models.CharField(max_length=20, default='Cylindrical 21700')
    mass = models.DecimalField(max_digits=10, decimal_places=2, default=70)
    mass_unit = models.CharField(max_length=1, choices={'g': 'Grams'}, default='g')
    height = models.DecimalField(max_digits=10, decimal_places=2, default=70.15)
    height_unit = models.CharField(max_length=2, choices={'mm': 'Millimeters'}, default='mm')
    diameter = models.DecimalField(max_digits=10, decimal_places=2, default=21.55)
    diameter_unit = models.CharField(max_length=2, choices={'mm': 'Millimeters'}, default='mm')
    volume = models.DecimalField(max_digits=10, decimal_places=2, default=25.59)
    volume = models.CharField(max_length=3, choices={'cm3': 'Cubic centimeter'}, default='mm')
    
    # ELECTRICAL PARAMETERS
    nominal_voltage = models.DecimalField(max_digits=10, decimal_places=2, default=3.6)
    nominal_voltage_unit = models.CharField(max_length=1, choices={'V': 'V'}, default='V')
    nominal_energy = models.DecimalField(max_digits=10, decimal_places=2, default=16.2)
    nominal_energy_unit = models.CharField(max_length=2, choices={'Wh': 'Wh'}, default='Wh')
    nominal_charge_capacity = models.DecimalField(max_digits=10, decimal_places=2, default=4.5)
    nominal_charge_capacity_unit = models.CharField(max_length=2, choices={'Ah': 'Ah'}, default='Ah')
    voltage_range = models.CharField(max_length=10, default='2.5-4.2')
    voltage_range_unit = models.CharField(max_length=1, choices={'V': 'V'}, default='V')
    current_continuous = models.DecimalField(max_digits=10, decimal_places=2, default=8.61)
    current_continuous_unit = models.CharField(max_length=1, choices={'A': 'A'}, default='A')
    current_peak = models.DecimalField(max_digits=10, decimal_places=2, default=17.5)
    current_peak_unit = models.CharField(max_length=1, choices={'A': 'A'}, default='A')
    power_continuous = models.DecimalField(max_digits=10, decimal_places=2, default=25.6)
    power_continuous_unit = models.CharField(max_length=1, choices={'W': 'W'}, default='W')
    power_peak = models.DecimalField(max_digits=10, decimal_places=2, default=50.0)
    power_peak_unit = models.CharField(max_length=1, choices={'W': 'W'}, default='W')
    energy_density_gravimetric = models.DecimalField(max_digits=10, decimal_places=2, default=154)
    energy_density_gravimetric_unit = models.CharField(max_length=5, choices={'Wh/kg': 'Wh/kg'}, default='Wh/kg')
    energy_density_volumetric = models.DecimalField(max_digits=10, decimal_places=2, default=375)
    energy_density_volumetric_unit = models.CharField(max_length=4, choices={'Wh/l': 'Wh/l'}, default='Wh/l')
    power_density_gravimetric = models.DecimalField(max_digits=10, decimal_places=2, default=837)
    power_density_gravimetric_unit = models.CharField(max_length=4, choices={'W/kg': 'W/kg'}, default='W/kg')
    power_density_volumetric = models.DecimalField(max_digits=10, decimal_places=2, default=2.04)
    power_density_volumetric_unit = models.CharField(max_length=4, choices={'kW/l': 'kW/l'}, default='kW/l')
    
    # override the save method so that 10 digit cell_id is generated on
    # basis of auto-incrementing 'id' AutoField
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.cell_id:
            self.cell_id = '{:010d}'.format(self.id)
            super().save(update_fields=['cell_id'])