# Generated by Django 3.0.4 on 2020-03-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
