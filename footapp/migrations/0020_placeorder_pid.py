# Generated by Django 4.2.7 on 2024-01-08 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('footapp', '0019_remove_placeorder_pid_remove_placeorder_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='pid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='footapp.shoesproduct'),
            preserve_default=False,
        ),
    ]
