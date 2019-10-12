# Generated by Django 2.2.5 on 2019-10-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_personinfo_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=60)),
                ('business_id', models.CharField(max_length=32)),
                ('group', models.CharField(max_length=32)),
                ('legal_person', models.CharField(max_length=10)),
                ('reg_fund', models.CharField(max_length=15)),
                ('staff_scale', models.CharField(max_length=10)),
                ('establishd_time', models.DateField(auto_now=True)),
            ],
        ),
    ]