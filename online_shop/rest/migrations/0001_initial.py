# Generated by Django 3.1.3 on 2020-11-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tea_types', models.CharField(choices=[('black', 'black'), ('green', 'green')], max_length=50)),
                ('price', models.IntegerField()),
                ('size', models.IntegerField(default=0)),
                ('tastes', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('products', models.ManyToManyField(to='rest.Product')),
            ],
        ),
    ]
