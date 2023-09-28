# Generated by Django 4.1.10 on 2023-09-23 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("population_data", "0014_alter_certainty_options_and_more"),
        ("property", "0005_remove_property_area_available_property_open"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="open",
        ),
        migrations.AddField(
            model_name="property",
            name="open",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="population_data.openclosesystem",
            ),
        ),
    ]
