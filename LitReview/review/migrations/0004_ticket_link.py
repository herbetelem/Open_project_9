# Generated by Django 4.0.6 on 2022-08-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_remove_ticket_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='link',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
