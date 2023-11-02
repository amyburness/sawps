# Generated by Django 4.1.10 on 2023-10-26 04:32

from django.db import migrations

from population_data.utils import (
    copy_owned_species_fields,
    assign_annual_population
)


def annual_population_forward_func(apps, schema_editor):
    AnnualPopulation = apps.get_model('population_data', 'AnnualPopulation')

    for annual_population in AnnualPopulation.objects.all():
        copy_owned_species_fields(annual_population)


def annual_population_reverse_func(apps, schema_editor):
    pass


def annual_population_activity_forward_func(apps, schema_editor):
    AnnualPopulationPerActivity = apps.get_model('population_data', 'AnnualPopulationPerActivity')
    AnnualPopulation = apps.get_model('population_data', 'AnnualPopulation')

    for annual_population_pa in AnnualPopulationPerActivity.objects.all():
        assign_annual_population(
            annual_population_pa,
            AnnualPopulation,
            AnnualPopulationPerActivity
        )


def annual_population_activity_reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("species", "0009_taxon_graph_icon"),
        (
            "population_data",
            "0016_remove_annualpopulationperactivity_unique_population_count_per_activity_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(annual_population_forward_func, annual_population_reverse_func),
        migrations.RunPython(annual_population_activity_forward_func, annual_population_activity_reverse_func),
    ]