# Generated by Django 5.0 on 2023-12-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_remove_pagecontact_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Сообщение'),
        ),
    ]
