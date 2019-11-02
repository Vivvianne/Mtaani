# Generated by Django 2.2.4 on 2019-08-13 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190813_1204'),
        ('neighbour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Neighbourhood'),
        ),
        migrations.DeleteModel(
            name='Neighbourhood',
        ),
    ]