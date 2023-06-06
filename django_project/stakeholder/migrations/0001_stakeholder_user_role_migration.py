# Generated by Django 4.1.7 on 2023-06-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='UserRoleType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'User role',
                'verbose_name_plural': 'User roles',
            },
        ),
    ]