# Generated by Django 5.0 on 2023-12-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_boss_remove_team_about_boss_remove_team_image_boss_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_team/', verbose_name='Фото Команды')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('work', models.CharField(max_length=255, verbose_name='Должность')),
                ('instagram', models.URLField(verbose_name='Инстаграм')),
                ('twitter', models.URLField(verbose_name='Вотсап')),
                ('facebook', models.URLField(verbose_name='Фейсбук')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
        ),
    ]
