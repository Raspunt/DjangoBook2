# Generated by Django 3.1.7 on 2021-04-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210412_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
