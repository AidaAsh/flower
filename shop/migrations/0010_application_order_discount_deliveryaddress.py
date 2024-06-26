# Generated by Django 5.0.4 on 2024-05-05 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_order_order_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_company', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_person_phone', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
                ('unp', models.CharField(max_length=255)),
                ('checking_account', models.CharField(max_length=255)),
                ('bank_code', models.CharField(max_length=255)),
                ('applications_per_month', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки корпоративные',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('apartment', models.CharField(max_length=255)),
                ('time', models.DateTimeField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
            options={
                'verbose_name': 'Адрес доставки',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
