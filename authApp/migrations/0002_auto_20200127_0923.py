# Generated by Django 3.0 on 2020-01-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='email',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='email_hash',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='first_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='ip',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='last_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='password',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='username',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.CharField(max_length=128),
        ),
    ]