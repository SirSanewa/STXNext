# Generated by Django 4.0.4 on 2022-05-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stx_api', '0004_rename_publish_year_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='stx_api.author'),
        ),
    ]
