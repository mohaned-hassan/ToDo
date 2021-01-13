# Generated by Django 3.0.8 on 2021-01-04 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0007_auto_20201228_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='CustomList',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Main.CustomList'),
        ),
    ]
