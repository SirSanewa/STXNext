# Generated by Django 4.0.4 on 2022-06-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stx_api', '0015_alter_book_acquired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
