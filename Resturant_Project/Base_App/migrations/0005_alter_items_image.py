# Generated by Django 5.0.6 on 2024-06-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0004_alter_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]