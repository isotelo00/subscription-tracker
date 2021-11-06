# Generated by Django 3.2.8 on 2021-11-06 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Subscrap', '0009_subscriptionlist_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionitem',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]