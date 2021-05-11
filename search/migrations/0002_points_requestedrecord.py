# Generated by Django 3.2 on 2021-05-11 04:36

from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0002_auto_20210511_1006'),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')], max_length=4, null=True)),
                ('units', models.IntegerField()),
                ('location', mapbox_location_field.models.LocationField(blank=True, map_attrs={'center': (77.21987228649732, 28.630981392199445), 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'}, null=True)),
                ('address', mapbox_location_field.models.AddressAutoHiddenField(blank=True, map_id='map', null=True)),
                ('contact_number', models.CharField(max_length=10)),
                ('emergency', models.CharField(blank=True, choices=[('urgently_required', 'Urgently Required'), ('pick_a_date', 'Pick a date')], max_length=18, null=True)),
                ('required_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('donor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreg.donorlist')),
                ('req_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.requestedrecord')),
            ],
        ),
    ]
