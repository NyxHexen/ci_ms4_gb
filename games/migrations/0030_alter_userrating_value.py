# Generated by Django 4.1.7 on 2023-04-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0029_alter_dlc_storyline_alter_game_storyline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='value',
            field=models.IntegerField(choices=[(0, '0 - None'), (1, '1 - Awful'), (2, '2 - Bad'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Very Good')], default='0'),
        ),
    ]