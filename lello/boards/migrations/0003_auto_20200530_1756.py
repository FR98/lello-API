# Generated by Django 3.0.6 on 2020-05-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200530_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='hours_done',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='list',
            name='hours_estimated',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
