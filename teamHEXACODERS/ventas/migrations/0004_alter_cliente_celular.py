# Generated by Django 5.1.2 on 2024-11-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_cliente_favoritos_producto_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
