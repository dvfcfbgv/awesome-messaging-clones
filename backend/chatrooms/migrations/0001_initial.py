# Generated by Django 2.1.5 on 2019-02-03 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChatroomMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('nickname', models.CharField(default='', max_length=25)),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='chatrooms.Chatroom')),
            ],
        ),
    ]