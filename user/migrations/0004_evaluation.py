# Generated by Django 2.1.7 on 2019-04-01 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_carer_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.TextField(max_length=100, verbose_name='建议')),
                ('q1', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q5', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q6', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q7', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q8', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q9', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q10', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q11', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q12', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q13', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q14', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q15', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q16', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q17', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('q18', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='护工美吗？')),
                ('carer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Carer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
