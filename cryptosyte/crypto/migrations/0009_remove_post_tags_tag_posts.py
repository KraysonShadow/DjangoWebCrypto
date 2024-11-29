# Generated by Django 5.0.2 on 2024-09-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0008_remove_tag_posts_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(related_name='tags', to='crypto.post'),
        ),
    ]