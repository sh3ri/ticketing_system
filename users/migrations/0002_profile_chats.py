# Generated by Django 2.2.4 on 2019-08-12 17:47

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='chats',
            field=jsonfield.fields.JSONField(default=[]),
        ),
    ]
