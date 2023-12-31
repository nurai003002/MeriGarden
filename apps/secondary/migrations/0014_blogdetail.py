# Generated by Django 5.0 on 2023-12-27 09:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0013_delete_gallerypluse'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions1', ckeditor.fields.RichTextField(verbose_name='Описание1')),
                ('letter', models.TextField(verbose_name='Письмо текст')),
                ('descriptions2', ckeditor.fields.RichTextField(verbose_name='Описание2')),
            ],
            options={
                'verbose_name': 'Описание новости',
                'verbose_name_plural': 'Описание новостей',
            },
        ),
    ]
