# Generated by Django 3.1.3 on 2020-11-17 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20201117_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='id',
            new_name='productId',
        ),
    ]