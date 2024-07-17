# Generated by Django 5.0.6 on 2024-07-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team/image', verbose_name='Фотография')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команда',
            },
        ),
    ]
