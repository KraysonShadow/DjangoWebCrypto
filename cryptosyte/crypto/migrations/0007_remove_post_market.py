# Generated by Django 5.0.2 on 2024-09-22 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0006_market_marketstats_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='market',
        ),
    ]