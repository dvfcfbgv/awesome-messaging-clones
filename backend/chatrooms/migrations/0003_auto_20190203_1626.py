# Generated by Django 2.1.5 on 2019-02-03 16:26

import backend.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0002_chatroommember_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='unique_identifier',
            field=models.CharField(default=backend.utils.id_generator, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]