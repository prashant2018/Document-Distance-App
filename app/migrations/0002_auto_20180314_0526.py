# Generated by Django 2.0.3 on 2018-03-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc1',
            field=models.TextField(max_length=200, verbose_name='Document 1'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc2',
            field=models.TextField(max_length=200, verbose_name='Document 2'),
        ),
    ]
