# Generated by Django 4.0.2 on 2022-02-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ce',
            name='firstname',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='ce',
            name='lastname',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
