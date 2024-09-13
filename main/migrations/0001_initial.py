# Generated by Django 5.1.1 on 2024-09-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('order_date', models.DateField()),
                ('order_status', models.CharField(max_length=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_items', models.IntegerField()),
                ('order_customer', models.CharField(max_length=50)),
                ('order_address', models.CharField(max_length=100)),
            ],
        ),
    ]
