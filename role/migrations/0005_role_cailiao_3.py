# Generated by Django 2.1.5 on 2019-05-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0004_auto_20190505_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='cailiao_3',
            field=models.IntegerField(default=0, verbose_name='三级材料'),
        ),
    ]
