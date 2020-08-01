# Generated by Django 2.2.5 on 2020-04-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('schId', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('branch', models.CharField(choices=[('CE', 'CE'), ('CSE', 'CSE'), ('ME', 'ME'), ('ECE', 'ECE'), ('EI', 'EI'), ('EE', 'EE')], default='CE', max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='HODRegister',
        ),
        migrations.DeleteModel(
            name='StudentRegister',
        ),
        migrations.AlterField(
            model_name='application',
            name='branch',
            field=models.CharField(choices=[('CE', 'CE'), ('CSE', 'CSE'), ('ME', 'ME'), ('ECE', 'ECE'), ('EI', 'EI'), ('EE', 'EE')], default='CE', max_length=6),
        ),
    ]
