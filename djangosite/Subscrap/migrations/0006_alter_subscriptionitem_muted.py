# Generated by Django 3.2.8 on 2021-11-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscrap', '0005_remove_subscriptionitem_tempid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionitem',
            name='muted',
            field=models.BooleanField(default=False),
        ),
    ]