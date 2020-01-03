# Generated by Django 2.2.4 on 2019-12-23 14:50

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('lemon_market2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='seller_id',
        ),
        migrations.AddField(
            model_name='group',
            name='bought_id',
            field=otree.db.models.PositiveIntegerField(choices=[(1, 'Buy from seller 1'), (2, 'Buy from seller 2'), (0, 'Buy nothing')], null=True),
        ),
    ]
