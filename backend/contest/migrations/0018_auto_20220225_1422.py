# Generated by Django 3.2.12 on 2022-02-25 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0017_alter_contest_allowed_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='prizes',
        ),
        migrations.CreateModel(
            name='ContestPrize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField()),
                ('name', models.TextField()),
                ('reward', models.TextField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
            ],
        ),
        migrations.AddField(
            model_name='acmcontestrank',
            name='prize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contest.contestprize'),
        ),
        migrations.AddField(
            model_name='oicontestrank',
            name='prize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contest.contestprize'),
        ),
    ]