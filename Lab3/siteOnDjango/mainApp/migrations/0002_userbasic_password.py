# Generated by Django 2.1.2 on 2018-10-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbasic',
            name='password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]