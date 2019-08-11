# Generated by Django 2.2.4 on 2019-08-11 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0003_auto_20190810_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.Neighbourhood'),
        ),
    ]
