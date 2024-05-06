# Generated by Django 5.0.4 on 2024-05-05 09:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_label_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='composition',
            options={'verbose_name': 'Состав букета', 'verbose_name_plural': 'Состав букетов'},
        ),
        migrations.AlterModelOptions(
            name='flower',
            options={'verbose_name': 'Цветок', 'verbose_name_plural': 'Цветы'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Состав заказа', 'verbose_name_plural': 'Состав заказов'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('id_product', 'email')},
        ),
        migrations.AlterIndexTogether(
            name='orderitem',
            index_together={('id_order', 'id_product')},
        ),
    ]
