# Generated by Django 3.0.6 on 2020-06-05 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_remove_card_checklist'),
        ('checklists', '0002_checklist_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='card',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checklist', to='boards.Card'),
        ),
    ]
