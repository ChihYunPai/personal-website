# Generated by Django 2.2 on 2019-05-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_product_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='---', max_length=10),
            preserve_default=False,
        ),
    ]
