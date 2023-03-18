# Generated by Django 4.1.7 on 2023-03-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_media_url_alter_developer_name_alter_developer_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dlc',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='esrbrating',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pegirating',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
