# Generated by Django 5.0.2 on 2024-09-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0007_remove_post_market'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='crypto.tag'),
        ),
    ]