# Generated by Django 3.2.8 on 2021-11-29 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_lesson', models.CharField(max_length=300)),
                ('knowledgeable', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.CharField(max_length=300)),
                ('d2', models.CharField(max_length=300)),
                ('numero', models.IntegerField(default=0)),
                ('knowledgeable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trying2.lesson')),
            ],
        ),
    ]
