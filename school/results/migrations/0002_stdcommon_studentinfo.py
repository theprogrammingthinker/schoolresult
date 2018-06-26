# Generated by Django 2.0.6 on 2018-06-25 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StdCommon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('stdcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.StdCommon')),
                ('std_name', models.CharField(max_length=100)),
                ('std_class', models.CharField(choices=[(6, 'SIX'), (7, 'SEVEN')], max_length=2)),
            ],
            bases=('results.stdcommon',),
        ),
    ]