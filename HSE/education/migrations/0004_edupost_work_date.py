# Generated by Django 3.2.4 on 2021-06-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_merge_0002_edupost_count_0002_edupost_work_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='edupost',
            name='work_date',
            field=models.DateTimeField(null=True),
        ),
    ]
