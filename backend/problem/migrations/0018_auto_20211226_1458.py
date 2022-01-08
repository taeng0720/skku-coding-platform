# Generated by Django 3.2.5 on 2021-12-26 05:58

from django.db import migrations, models
import problem.models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0017_auto_20210814_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='io_mode',
            field=models.JSONField(default=problem.models._default_io_mode),
        ),
        migrations.AlterField(
            model_name='problem',
            name='languages',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='samples',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statistic_info',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='problem',
            name='template',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='test_case_score',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='problemtag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]