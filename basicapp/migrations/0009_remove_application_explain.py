# Generated by Django 2.2.5 on 2020-07-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0008_auto_20200715_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='explain',
        ),
    ]
