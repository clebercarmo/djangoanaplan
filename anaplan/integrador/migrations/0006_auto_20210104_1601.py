# Generated by Django 3.1.4 on 2021-01-04 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('integrador', '0005_auto_20210104_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='execucao',
            name='processlist',
        ),
        migrations.RemoveField(
            model_name='processlist',
            name='modelo',
        ),
        migrations.AddField(
            model_name='processlist',
            name='execucao',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='execucao_processlist', to='integrador.execucao', verbose_name='Execucao'),
            preserve_default=False,
        ),
    ]