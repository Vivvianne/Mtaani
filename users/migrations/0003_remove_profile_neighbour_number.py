# Generated by Django 2.2.4 on 2019-08-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190810_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighbour_number',
        ),
    ]