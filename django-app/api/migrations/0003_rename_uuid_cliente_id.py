# Generated by Django 4.2.1 on 2023-10-04 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_cliente_id_cliente_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='uuid',
            new_name='id',
        ),
    ]
