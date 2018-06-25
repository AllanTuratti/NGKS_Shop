# Generated by Django 2.0.6 on 2018-06-24 15:17

import SGU.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=150)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', SGU.models.UsuarioManager()),
            ],
        ),
        migrations.AddField(
            model_name='permissions',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='SGU.usuario'),
        ),
    ]
