# Generated by Django 5.1.4 on 2025-01-06 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountRoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleType', models.CharField(choices=[('ADMIN', 'Admin'), ('NORMAL', 'Normal'), ('SUBSCRIBE', 'Subscribe')], default='NORMAL', max_length=64)),
            ],
            options={
                'db_table': 'account_role_type',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32)),
                ('roleType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kakao_account.accountroletype')),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]
