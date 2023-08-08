# Generated by Django 4.2.2 on 2023-08-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='author',
            old_name='date_of_birth',
            new_name='year_of_birth',
        ),
    ]
