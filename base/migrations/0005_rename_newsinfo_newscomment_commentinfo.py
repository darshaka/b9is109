# Generated by Django 4.0.3 on 2022-06-26 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_newscomment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newscomment',
            old_name='newsInfo',
            new_name='commentInfo',
        ),
    ]
