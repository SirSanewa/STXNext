# Generated by Django 4.0.4 on 2022-06-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stx_api', '0014_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='acquired',
            field=models.BooleanField(default=False),
        ),
    ]