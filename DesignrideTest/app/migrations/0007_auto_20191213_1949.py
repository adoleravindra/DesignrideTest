# Generated by Django 2.2.6 on 2019-12-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191213_1425'),
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
