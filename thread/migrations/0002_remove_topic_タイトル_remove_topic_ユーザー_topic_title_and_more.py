# Generated by Django 4.0.3 on 2022-04-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='タイトル',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='ユーザー',
        ),
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
