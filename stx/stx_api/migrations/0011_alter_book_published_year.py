# Generated by Django 4.0.4 on 2022-05-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stx_api', '0010_alter_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(null=True),
        ),
    ]
