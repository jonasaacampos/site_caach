# Generated by Django 5.0.4 on 2024-05-09 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_entity', '0017_alter_sitefooter_main_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company_entity.company')),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': 'Parceiros',
                'ordering': ['id'],
            },
            bases=('company_entity.company',),
        ),
        migrations.AddField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='Razão Social'),
        ),
    ]
