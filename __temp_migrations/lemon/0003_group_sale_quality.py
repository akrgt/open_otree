# Generated by Django 2.2.4 on 2020-02-08 03:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('lemon', '0002_auto_20200208_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='sale_quality',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]