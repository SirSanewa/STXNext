# Generated by Django 4.0.4 on 2022-05-29 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stx_api', '0002_alter_book_book_external_id_alter_book_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_external_id',
            new_name='external_id',
        ),
    ]
