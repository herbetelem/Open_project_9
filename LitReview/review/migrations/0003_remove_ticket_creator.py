# Generated by Django 4.0.6 on 2022-08-25 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_ticket_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='creator',
        ),
    ]
