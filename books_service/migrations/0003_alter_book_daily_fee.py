# Generated by Django 5.0.7 on 2024-09-26 13:28

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_service', '0002_alter_book_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='daily_fee',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
