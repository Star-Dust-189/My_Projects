# Generated by Django 4.1.6 on 2023-03-10 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue_provider',
            name='Venue_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tables.venue_type'),
        ),
    ]
