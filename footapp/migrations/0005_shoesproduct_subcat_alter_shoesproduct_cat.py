# Generated by Django 4.2.7 on 2024-01-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footapp', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoesproduct',
            name='subcat',
            field=models.IntegerField(choices=[(1, 'All'), (2, 'athletic'), (3, 'casual'), (4, 'boots'), (5, 'sandals'), (6, 'formal'), (7, 'slippers')], default=None),
        ),
        migrations.AlterField(
            model_name='shoesproduct',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Men'), (2, 'Women'), (3, 'Child'), (4, 'newdeals')]),
        ),
    ]
