# Generated by Django 3.0 on 2019-12-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopicmodel',
            name='body_article',
            field=models.TextField(blank=True),
        ),
    ]
