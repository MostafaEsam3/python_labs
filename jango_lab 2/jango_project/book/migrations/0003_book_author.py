# Generated by Django 5.0.4 on 2024-05-08 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0002_book_image_book_latest_version_book_publish_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
            preserve_default=False,
        ),
    ]
