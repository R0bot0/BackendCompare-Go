# Generated by Django 4.0.4 on 2022-04-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidCasesCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_region', models.CharField(max_length=100)),
                ('confirmed', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('active', models.IntegerField()),
                ('new_cases', models.IntegerField()),
                ('new_deaths', models.IntegerField()),
                ('new_recovered', models.IntegerField()),
                ('deaths_100cases', models.FloatField()),
                ('recovered_100cases', models.FloatField()),
                ('deaths_100recovered', models.FloatField()),
                ('confirmed_lastweek', models.IntegerField()),
                ('oneweek_change', models.IntegerField()),
                ('oneweek_percincrease', models.FloatField()),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CovidCasesDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('confirmed', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('active', models.IntegerField()),
                ('new_cases', models.IntegerField()),
                ('new_deaths', models.IntegerField()),
                ('new_recovered', models.IntegerField()),
                ('deaths_100cases', models.FloatField()),
                ('recovered_100cases', models.FloatField()),
                ('deaths_100recovered', models.FloatField()),
                ('num_countries', models.IntegerField()),
            ],
        ),
    ]
