# Generated by Django 4.2.7 on 2023-12-19 19:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('computer', 'Computer'), ('monitor', 'Monitor'), ('keyboard', 'Keyboard')], max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('processor', models.CharField(max_length=50)),
                ('graphics', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('computer', 'Computer'), ('monitor', 'Monitor'), ('keyboard', 'Keyboard')], max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('key_switch_type', models.CharField(choices=[('membrane', 'Membrane'), ('mechanical', 'Mechanical'), ('scissor', 'Scissor')], max_length=30)),
                ('backlight', models.BooleanField(default=False)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('wireless', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('computer', 'Computer'), ('monitor', 'Monitor'), ('keyboard', 'Keyboard')], max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('resolution', models.CharField(max_length=20)),
                ('refresh_rate', models.CharField(max_length=10)),
                ('panel_type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
