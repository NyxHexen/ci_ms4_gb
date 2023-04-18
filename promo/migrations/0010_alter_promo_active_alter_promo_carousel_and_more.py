# Generated by Django 4.1.7 on 2023-04-18 10:34

from django.db import migrations, models
import django.db.models.deletion
import promo.utils


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('promo', '0009_alter_promo_apply_to_dlc_alter_promo_apply_to_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active?'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='carousel',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add to Home Carousel'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='end_date',
            field=models.DateTimeField(default=promo.utils.default_end_datetime, null=True, verbose_name='End On'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add to Featured List'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='landing_page',
            field=models.BooleanField(default=False, verbose_name='Landing Page?'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.media'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='name',
            field=models.CharField(max_length=254, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='start_date',
            field=models.DateTimeField(default=promo.utils.default_start_datetime, null=True, verbose_name='Start From'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='url',
            field=models.URLField(blank=True, max_length=1024, null=True, verbose_name='URL'),
        ),
    ]