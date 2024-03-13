# Generated by Django 5.0.3 on 2024-03-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_batterycell_volume_unit_alter_batterycell_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterycell',
            name='volume_unit',
            field=models.CharField(choices=[('cm3', 'Cubic centimeter')], default='cm3', max_length=3),
        ),
    ]
