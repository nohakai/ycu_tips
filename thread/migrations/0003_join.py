# Generated by Django 4.0.3 on 2022-04-17 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_remove_topic_タイトル_remove_topic_ユーザー_topic_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='thread.topic')),
            ],
        ),
    ]
