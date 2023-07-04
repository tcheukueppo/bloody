# Generated by Django 4.1.7 on 2023-07-04 09:13

import bloody.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='health_center',
            fields=[
                ('name', models.TextField(max_length=256, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.ImageField(upload_to=bloody.models.health_center.upload)),
            ],
        ),
        migrations.CreateModel(
            name='health_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.ImageField(upload_to=bloody.models.health_person.upload)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloody.health_center')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='donator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('tel', models.TextField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('profile', models.ImageField(upload_to=bloody.models.donator.upload)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A+', 'A positive'), ('A-', 'A negative'), ('B+', 'B positive'), ('B-', 'B negative'), ('AB+', 'AB positive'), ('AB-', 'AB negative'), ('O+', 'O positive'), ('O-', 'O negative')], max_length=3)),
                ('age', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloody.health_person')),
                ('donator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloody.donator')),
            ],
        ),
        migrations.CreateModel(
            name='demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A+', 'A positive'), ('A-', 'A negative'), ('B+', 'B positive'), ('B-', 'B negative'), ('AB+', 'AB positive'), ('AB-', 'AB negative'), ('O+', 'O positive'), ('O-', 'O negative')], max_length=3)),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=2)),
                ('date', models.DateTimeField()),
                ('location', models.TextField(blank=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloody.health_person')),
            ],
        ),
    ]
