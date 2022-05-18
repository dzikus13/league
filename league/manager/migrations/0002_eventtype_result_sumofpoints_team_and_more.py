# Generated by Django 4.0.4 on 2022-05-12 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SumOfPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(max_length=10)),
                ('matches_won', models.IntegerField()),
                ('matches_draw', models.IntegerField()),
                ('matches_lost', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='league',
            name='max_number_of_teams',
            field=models.IntegerField(default=16, verbose_name=10),
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('nick', models.CharField(max_length=20)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.league'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('result', models.CharField(max_length=20, null=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.league')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.eventtype')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.teamplayer')),
            ],
        ),
    ]