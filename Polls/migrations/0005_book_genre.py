# Generated by Django 3.1.7 on 2021-03-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0004_auto_20210317_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Genre',
            field=models.ManyToManyField(blank=True, to='Polls.Genre'),
        ),
    ]