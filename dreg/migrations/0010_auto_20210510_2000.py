# Generated by Django 3.2 on 2021-05-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0009_alter_donorlist_last_donate_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='donorlist',
            name='donation_record',
            field=models.ManyToManyField(to='dreg.DonationDate'),
        ),
    ]