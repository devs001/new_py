# Generated by Django 3.0.7 on 2020-07-01 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0004_auto_20200630_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='header',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artical.Head'),
        ),
    ]
