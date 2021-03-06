# Generated by Django 3.2 on 2021-04-11 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210411_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='display',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.display'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gpu',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.gpu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='harddisk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.harddisk'),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.processor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.ram'),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.storage'),
        ),
    ]
