# Generated by Django 4.0.2 on 2022-04-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='grade',
            new_name='semester',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='roll',
        ),
        migrations.AddField(
            model_name='payments',
            name='entry',
            field=models.CharField(default=123, max_length=12),
            preserve_default=False,
        ),
    ]
