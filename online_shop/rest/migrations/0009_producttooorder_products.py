# Generated by Django 3.1.3 on 2020-11-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_auto_20201124_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttooorder',
            name='products',
            field=models.ManyToManyField(to='rest.Product'),
        ),
    ]
