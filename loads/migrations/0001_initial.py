# Generated by Django 4.2.3 on 2023-07-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goat_count', models.IntegerField(default=0)),
                ('num_male', models.IntegerField(default=0)),
                ('num_female', models.IntegerField(default=0)),
                ('value_load', models.FloatField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]