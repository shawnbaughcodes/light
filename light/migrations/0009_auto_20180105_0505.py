# Generated by Django 2.0.1 on 2018-01-05 05:05

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0008_auto_20170719_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='json',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='media',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
