# Generated by Django 4.2.7 on 2023-12-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footapp', '0002_shoesproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoesproduct',
            name='brand',
            field=models.CharField(default='No name', max_length=50),
        ),
    ]
