# Generated by Django 2.2 on 2021-07-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0018_auto_20210710_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='nb_animal_num',
            field=models.IntegerField(default=0, verbose_name='强力珍兽数量'),
        ),
    ]
