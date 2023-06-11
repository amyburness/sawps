# Generated by Django 4.1.7 on 2023-06-09 18:04

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    replaces = [
        ("property", "0001_initial"),
        ("property", "0002_parceltype_parcel"),
        ("property", "0003_parcel_property"),
    ]

    initial = True

    dependencies = [
        ("stakeholder", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OwnershipStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "ownership status",
                "verbose_name_plural": "ownership status",
                "db_table": "ownership_status",
            },
        ),
        migrations.CreateModel(
            name="PropertyType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
            ],
            options={
                "verbose_name": "Property type",
                "verbose_name_plural": "Property types",
                "db_table": "property_type",
            },
        ),
        migrations.CreateModel(
            name="Province",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Province",
                "verbose_name_plural": "Provinces",
                "db_table": "province",
            },
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, unique=True)),
                (
                    "owner_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("property_size_ha", models.IntegerField(blank=True, null=True)),
                ("area_available", models.FloatField()),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("created_at", models.DateTimeField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organisation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="stakeholder.organisation",
                    ),
                ),
                (
                    "ownership_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="property.ownershipstatus",
                    ),
                ),
                (
                    "property_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="property.propertytype",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="property.province",
                    ),
                ),
            ],
            options={
                "verbose_name": "Property",
                "verbose_name_plural": "Properties",
                "db_table": "property",
            },
        ),
        migrations.AddConstraint(
            model_name="property",
            constraint=models.CheckConstraint(
                check=models.Q(("area_available__lte", models.F("property_size_ha"))),
                name="check property size",
            ),
        ),
        migrations.CreateModel(
            name="ParcelType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Parcel type",
                "verbose_name_plural": "Parcel types",
                "db_table": "parcel_type",
            },
        ),
        migrations.CreateModel(
            name="Parcel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sg_number", models.CharField(max_length=100, unique=True)),
                ("year", models.DateField()),
                (
                    "parcel_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="property.parceltype",
                    ),
                ),
                (
                    "property",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="property.property",
                    ),
                ),
            ],
            options={
                "verbose_name": "Parcel",
                "verbose_name_plural": "Parcels",
                "db_table": "parcel",
            },
        ),
    ]