# Generated by Django 4.2.6 on 2023-10-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_palindromegame_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palindromegame',
            name='value',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]