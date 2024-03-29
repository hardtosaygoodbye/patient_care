# Generated by Django 2.1.7 on 2019-04-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190401_0733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carer',
            name='num_family',
        ),
        migrations.RemoveField(
            model_name='carer',
            name='num_hospital',
        ),
        migrations.RemoveField(
            model_name='carer',
            name='num_patient',
        ),
        migrations.RemoveField(
            model_name='carer',
            name='score',
        ),
        migrations.AddField(
            model_name='carer',
            name='family_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='医院均分'),
        ),
        migrations.AddField(
            model_name='carer',
            name='hospital_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='医院均分'),
        ),
        migrations.AddField(
            model_name='carer',
            name='patient_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='病人均分'),
        ),
        migrations.AddField(
            model_name='carer',
            name='total_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='总分'),
        ),
    ]
