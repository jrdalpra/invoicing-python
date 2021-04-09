# Generated by Django 3.1.7 on 2021-04-09 13:22

from django.db import migrations, models
import modules.core.models.definitions
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210409_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='marketable',
            name='kind',
            field=models.CharField(blank=True, choices=[('Product', 'PRODUCT'), ('Service', 'SERVICE')], default=modules.core.models.definitions.MarketableKind['PRODUCT'], max_length=1024, verbose_name='Kind'),
        ),
    ]
