# Generated by Django 2.2.6 on 2019-12-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AlterField(
            model_name='products',
            name='ProductName',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]