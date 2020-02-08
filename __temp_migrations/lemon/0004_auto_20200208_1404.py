# Generated by Django 2.2.4 on 2020-02-08 05:04

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('lemon', '0003_group_sale_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='sale_price',
            field=otree.db.models.CurrencyField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='sale_quality',
            field=otree.db.models.StringField(default='', max_length=10000, null=True),
        ),
    ]