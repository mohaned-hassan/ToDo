# Generated by Django 3.0.8 on 2021-01-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_remove_task_lol'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='lol',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
