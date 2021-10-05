# Generated by Django 3.2.7 on 2021-10-05 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('ciudad', models.CharField(max_length=50, unique=True, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['ciudad'],
            },
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='rutas.ciudad')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='rutas.ciudad')),
            ],
            options={
                'verbose_name': 'Trayecto',
                'verbose_name_plural': 'Trayectos',
                'ordering': ['id', 'origen', 'destino'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalTrayecto',
            fields=[
                ('id', models.CharField(db_index=True, max_length=50, verbose_name='id')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('destino', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='rutas.ciudad')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('origen', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='rutas.ciudad')),
            ],
            options={
                'verbose_name': 'historical Trayecto',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCiudad',
            fields=[
                ('id', models.CharField(db_index=True, max_length=5, verbose_name='id')),
                ('ciudad', models.CharField(db_index=True, max_length=50, verbose_name='Ciudad')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Ciudad',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
