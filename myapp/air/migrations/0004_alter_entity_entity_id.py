# Generated by Django 5.0.4 on 2024-04-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0003_alter_entitydata_entity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='entity_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
