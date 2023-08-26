# Generated by Django 4.2.2 on 2023-08-26 01:37

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_author_year_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='year_of_birth',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), catalog.models.max_value_from_current_year]),
        ),
        migrations.AlterField(
            model_name='author',
            name='year_of_death',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
