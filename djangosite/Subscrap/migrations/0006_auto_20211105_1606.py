# Generated by Django 3.2.8 on 2021-11-05 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subscrap', '0005_remove_subscriptionitem_tempid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionitem',
            name='cyclePeriod',
        ),
        migrations.RemoveField(
            model_name='subscriptionitem',
            name='postitionInList',
        ),
        migrations.RemoveField(
            model_name='subscriptionitem',
            name='price',
        ),
    ]
