# Generated by Django 4.0.6 on 2022-08-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='creator',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
    ]
