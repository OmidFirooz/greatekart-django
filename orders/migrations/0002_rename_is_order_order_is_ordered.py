# Generated by Django 4.1.7 on 2023-08-26 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_order',
            new_name='is_ordered',
        ),
    ]
