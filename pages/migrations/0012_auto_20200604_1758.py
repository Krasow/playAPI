# Generated by Django 3.0.6 on 2020-06-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20200604_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='code',
            field=models.CharField(default=564465, help_text='Enter Verification Code', max_length=12),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='VerifyModel',
        ),
    ]
