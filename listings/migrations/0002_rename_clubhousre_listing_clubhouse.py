# Generated by Django 5.2.1 on 2025-05-29 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='clubhousre',
            new_name='clubhouse',
        ),
    ]
