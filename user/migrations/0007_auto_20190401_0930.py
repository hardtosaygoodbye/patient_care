# Generated by Django 2.1.7 on 2019-04-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190401_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='carer',
            name='family_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carer',
            name='hospital_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carer',
            name='patient_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carer',
            name='family_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='家属均分'),
        ),
    ]
