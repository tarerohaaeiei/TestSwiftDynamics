# Generated by Django 4.2.3 on 2023-07-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.CharField(max_length=80),
        ),
    ]