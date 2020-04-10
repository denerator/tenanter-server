# Generated by Django 3.0.4 on 2020-04-10 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_flats', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signing_date', models.DateField()),
                ('payment_day', models.IntegerField()),
                ('contract_time', models.IntegerField()),
                ('rental_rate', models.IntegerField()),
                ('deposit', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('flat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tenant', to='flat.Flat')),
            ],
        ),
    ]
