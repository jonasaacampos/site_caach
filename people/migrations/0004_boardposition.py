# Generated by Django 5.0.4 on 2024-04-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_people_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardPosition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
