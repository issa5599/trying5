# Generated by Django 3.2.8 on 2021-11-29 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trying2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='knowledgeable',
            new_name='all_lesson',
        ),
    ]
