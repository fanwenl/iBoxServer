# Generated by Django 2.0.7 on 2018-08-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180804_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dac',
            options={'ordering': ['-time']},
        ),
        migrations.AlterField(
            model_name='dac',
            name='data',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='dac',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='msg',
            name='eth_mac',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='msg',
            name='wifi_mac',
            field=models.CharField(max_length=20),
        ),
    ]
