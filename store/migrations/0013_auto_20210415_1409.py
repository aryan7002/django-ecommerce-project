# Generated by Django 3.2 on 2021-04-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_storage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processor',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
