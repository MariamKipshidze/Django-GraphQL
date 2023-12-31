# Generated by Django 4.2.7 on 2023-11-29 09:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('ingredients', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Ingredients')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
