# Generated by Django 4.0.4 on 2022-05-30 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stx_api', '0003_rename_book_external_id_book_external_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_year',
            new_name='published_year',
        ),
    ]
