# Generated by Django 2.1.5 on 2019-02-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20190224_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='initial_profiles/194.jpg', upload_to='profile_pics'),
        ),
    ]
