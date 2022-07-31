# Generated by Django 4.0.6 on 2022-07-31 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_e6a359_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]
