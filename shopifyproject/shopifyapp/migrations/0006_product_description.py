# Generated by Django 4.2.16 on 2024-10-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyapp', '0005_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
