# Generated by Django 3.1.7 on 2021-03-08 13:30

from django.db import migrations, models
import modules.core.models.definitions
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('klass', models.CharField(blank=True, choices=[('Product', 'PRODUCT'), ('Service', 'SERVICE')], default=modules.core.models.definitions.MarketableKind['PRODUCT'], max_length=1024, verbose_name='Class')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
