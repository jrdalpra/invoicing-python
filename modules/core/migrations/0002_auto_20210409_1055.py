# Generated by Django 3.1.7 on 2021-04-09 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketable',
            old_name='klass',
            new_name='kind',
        ),
    ]
