# Generated by Django 2.1.5 on 2019-02-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190218_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='initial_profiles/305.jpg', upload_to='profile_pics'),
        ),
    ]
