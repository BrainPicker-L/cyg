# Generated by Django 2.2 on 2021-06-14 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0016_auto_20210315_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='attack_all_value',
        ),
        migrations.RemoveField(
            model_name='role',
            name='nb_xinjue_name',
        ),
        migrations.RemoveField(
            model_name='role',
            name='nb_xinjue_num',
        ),
        migrations.RemoveField(
            model_name='role',
            name='shizhuang_name',
        ),
    ]