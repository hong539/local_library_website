# Generated by Django 4.2.2 on 2023-06-24 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text='Enter one author for this book. If dual/triple or more authors is not wokring', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Enter a book title (e.g. The Linux Programming Interface)', max_length=200),
        ),
    ]
