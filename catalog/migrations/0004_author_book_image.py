# Generated by Django 5.0.2 on 2024-03-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_author_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
