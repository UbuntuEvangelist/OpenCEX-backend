# Generated by Django 3.2.18 on 2023-08-04 08:38

from django.db import migrations
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_pair_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairsettings',
            name='min_base_amount_increment',
            field=lib.fields.MoneyField(decimal_places=8, default=0.0, max_digits=32),
        ),
        migrations.AddField(
            model_name='pairsettings',
            name='min_order_size',
            field=lib.fields.MoneyField(decimal_places=8, default=0.0, max_digits=32),
        ),
        migrations.AddField(
            model_name='pairsettings',
            name='min_price_increment',
            field=lib.fields.MoneyField(decimal_places=8, default=0.0, max_digits=32),
        ),
    ]
