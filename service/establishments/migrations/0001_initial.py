# Generated by Django 4.1 on 2024-06-06 18:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('build_number', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=30)),
                ('short_description', models.TextField(max_length=1000)),
                ('capacity', models.IntegerField()),
                ('work_mobile_number', models.CharField(max_length=30)),
                ('is_recommended', models.BooleanField(default=False)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='establishments.address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PriceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_range', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('establishments', models.ManyToManyField(related_name='services', to='establishments.establishment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EstablishmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='establishment_images')),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='establishments.establishment')),
            ],
        ),
        migrations.AddField(
            model_name='establishment',
            name='price_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishments.pricecategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('content', models.TextField(verbose_name=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='establishments.establishment')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('establishments', models.ManyToManyField(related_name='amenities', to='establishments.establishment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]