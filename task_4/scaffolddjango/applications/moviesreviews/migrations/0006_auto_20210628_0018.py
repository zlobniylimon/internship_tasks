# Generated by Django 3.2.4 on 2021-06-27 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesreviews', '0005_auto_20210627_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='content',
        ),
    ]
