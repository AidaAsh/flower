# Generated by Django 5.0.4 on 2024-05-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_id_category_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productcategories',
            unique_together={('id_category', 'id_product')},
        ),
    ]
