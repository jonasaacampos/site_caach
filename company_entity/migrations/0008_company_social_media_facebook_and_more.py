# Generated by Django 5.0.4 on 2024-05-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_entity', '0007_alter_sitefooter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='social_media_facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='company',
            name='social_media_instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='company',
            name='social_media_linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='company',
            name='social_media_whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='WhatsApp'),
        ),
    ]
