# Generated by Django 3.1.7 on 2021-03-17 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0003_auto_20210317_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='genreTree',
        ),
    ]
