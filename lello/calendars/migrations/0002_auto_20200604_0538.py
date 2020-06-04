# Generated by Django 3.0.6 on 2020-06-04 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20200530_1756'),
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar', to='boards.Board'),
        ),
    ]