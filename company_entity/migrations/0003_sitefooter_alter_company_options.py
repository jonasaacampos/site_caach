# Generated by Django 5.0.4 on 2024-05-06 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_entity', '0002_alter_company_options_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteFooter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome do rodapé (controle interno)')),
                ('service_hours', models.CharField(max_length=100, verbose_name='Horário de Atendimento')),
                ('line_text1', models.CharField(max_length=200, verbose_name='Texto da Linha 1')),
                ('line_text2', models.CharField(max_length=200, verbose_name='Texto da Linha 2')),
            ],
            options={
                'verbose_name': 'Rodapé do Site',
                'verbose_name_plural': 'Rodapés do Site',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['company_name'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
    ]
