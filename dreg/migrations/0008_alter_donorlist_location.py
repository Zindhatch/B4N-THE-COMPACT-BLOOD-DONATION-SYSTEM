# Generated by Django 3.2 on 2021-05-08 14:30

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0007_alter_donorlist_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorlist',
            name='location',
            field=mapbox_location_field.models.LocationField(blank=True, map_attrs={'center': (77.1025, 28.7041), 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'}, null=True),
        ),
    ]
