# Generated by Django 3.1.7 on 2022-07-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=255),
        ),
    ]
