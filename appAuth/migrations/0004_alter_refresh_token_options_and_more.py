# Generated by Django 4.2.15 on 2024-09-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAuth', '0003_refresh_token_delete_amazonauth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refresh_token',
            options={'verbose_name': 'Refresh Token', 'verbose_name_plural': 'Refresh Tokens'},
        ),
        migrations.AddField(
            model_name='refresh_token',
            name='access_token',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='refresh_token',
            name='seller_id',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
