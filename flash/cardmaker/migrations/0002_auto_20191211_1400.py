# Generated by Django 3.0 on 2019-12-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardmaker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='subject',
            new_name='stack',
        ),
        migrations.AddField(
            model_name='stack',
            name='title',
            field=models.CharField(default='dummy', max_length=200),
            preserve_default=False,
        ),
    ]
