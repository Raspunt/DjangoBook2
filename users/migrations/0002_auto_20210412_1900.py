# Generated by Django 3.1.7 on 2021-04-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rating',
            field=models.FloatField(blank=True),
        ),
    ]
