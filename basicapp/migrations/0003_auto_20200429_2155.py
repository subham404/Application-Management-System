# Generated by Django 2.2.5 on 2020-04-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp','__first__'),
        ('basicapp', '0002_auto_20200429_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='id',
            field=models.AutoField(auto_created=True, default=103, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='schId',
            field=models.SmallIntegerField(default='', editable=False, max_length=10, unique=True),
        ),
    ]
