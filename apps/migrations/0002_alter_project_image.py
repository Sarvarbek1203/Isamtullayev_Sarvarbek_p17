# Generated by Django 5.0.2 on 2024-02-15 11:49

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='project/default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[400, 150], upload_to='project/images'),
        ),
    ]
