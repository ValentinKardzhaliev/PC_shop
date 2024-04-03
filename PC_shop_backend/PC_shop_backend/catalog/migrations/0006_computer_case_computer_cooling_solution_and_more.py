# Generated by Django 4.2.7 on 2024-04-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_keyboard_brand_keyboard_format_keyboard_key_rollover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='case',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='cooling_solution',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='network',
            field=models.CharField(blank=True, choices=[('ethernet', 'Ethernet'), ('wifi', 'Wi-Fi'), ('bluetooth', 'Bluetooth')], max_length=20, null=True),
        ),
    ]
