# Generated by Django 3.1.3 on 2020-11-17 06:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20201117_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
