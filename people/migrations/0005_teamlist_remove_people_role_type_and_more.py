# Generated by Django 5.0.4 on 2024-04-29 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_boardposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='people',
            name='role_type',
        ),
        migrations.AddField(
            model_name='people',
            name='board_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='board_position', to='people.boardposition'),
        ),
        migrations.AddField(
            model_name='people',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='people_team', to='people.teamlist'),
        ),
    ]
