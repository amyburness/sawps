# Generated by Django 4.1.7 on 2023-06-13 04:08

from django.db import migrations


class Migration(migrations.Migration):
    """Add new tables for parcel label layer."""
    dependencies = [
        ("frontend", "0002_erf_farmportion_holding_parentfarm"),
    ]

    operations = [
        migrations.RunSQL(
            """create table if not exists layer.farm_portion_labels as
            select id as id,
                st_pointonsurface(st_makevalid(geom)) as geom,
                tag_value as tag_value,
                cname as cname
            from layer.farm_portion""",
            reverse_sql="drop table if exists layer.farm_portion_labels",
            elidable=False
        ),
        migrations.RunSQL(
            """create table if not exists layer.holding_labels as
            select id as id,
                st_pointonsurface(st_makevalid(geom)) as geom,
                tag_value as tag_value,
                cname as cname
            from layer.holding""",
            reverse_sql="drop table if exists layer.holding_labels",
            elidable=False
        ),
        migrations.RunSQL(
            """create table if not exists layer.erf_labels as
            select id as id,
                st_pointonsurface(st_makevalid(geom)) as geom,
                tag_value as tag_value,
                cname as cname
            from layer.erf""",
            reverse_sql="drop table if exists layer.erf_labels",
            elidable=False
        ),
    ]