# Generated by Django 2.2 on 2021-03-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0008_remove_role_miji'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='diaowen8',
            field=models.IntegerField(default=0, verbose_name='8级雕文数量'),
        ),
    ]
