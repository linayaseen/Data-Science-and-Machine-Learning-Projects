# Generated by Django 4.2.1 on 2023-06-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_patient_caa_patient_oldpeak_patient_slp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='thalachh',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
