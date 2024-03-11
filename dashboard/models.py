from django.db import models

class BatteryCell(models.Model):
    # image is stored as a base64 encoded data url
    image_data_url = models.TextField()
    cell_id = models.CharField(max_length=10, blank=True)
    
    # override the save method so that 10 digit cell_id is generated on
    # basis of auto-incrementing 'id' AutoField
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.cell_id:
            self.cell_id = '{:010d}'.format(self.id)
            super().save(update_fields=['cell_id'])