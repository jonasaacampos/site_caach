# Generated by Django 5.0.4 on 2024-05-08 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_entity', '0004_alter_company_address_alter_company_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
    ]
