# Generated by Django 4.0.4 on 2022-05-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0003_alter_strategy_best_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='best_config',
            field=models.JSONField(blank=True, default={'Empty': 'Empty'}),
        ),
    ]
