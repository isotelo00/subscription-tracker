# Generated by Django 3.2.8 on 2021-11-06 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subscrap', '0006_alter_subscriptionitem_muted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionitem',
            name='SubscriptionList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Subscrap.subscriptionlist'),
        ),
    ]
