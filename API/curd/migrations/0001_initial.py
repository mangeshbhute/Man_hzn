# Generated by Django 3.2.8 on 2022-02-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodect_Details',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('quan', models.IntegerField()),
                ('buyer', models.BooleanField()),
            ],
        ),
    ]
