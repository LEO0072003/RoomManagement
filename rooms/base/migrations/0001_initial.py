# Generated by Django 4.0.5 on 2022-10-31 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, max_length=10, null=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=10)),
                ('event_type', models.TextField(choices=[('public', 'public'), ('private', 'private')], max_length=10)),
                ('event', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='base.rooms')),
            ],
        ),
    ]
