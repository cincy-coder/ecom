# Generated by Django 5.1.4 on 2025-01-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0012_delete_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Return', 'Return')], default='Pending', max_length=54),
        ),
    ]
