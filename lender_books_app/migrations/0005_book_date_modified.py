# Generated by Django 2.1.7 on 2019-03-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lender_books_app', '0004_book_last_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]