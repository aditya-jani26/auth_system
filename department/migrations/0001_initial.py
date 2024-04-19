# Generated by Django 5.0.4 on 2024-04-19 09:34

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=50)),
                ('userType', models.CharField(choices=[('Admin', 'Admin'), ('Project_Manager', 'Project_Manager'), ('Team_Leader', 'Team_Leader'), ('Employee', 'Employee')], max_length=100)),
                ('allocation_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlacklistedToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=50)),
                ('projectDescription', models.CharField(max_length=500)),
                ('projectStartDate', models.DateField(default=django.utils.timezone.now)),
                ('projectEndDate', models.DateField(null=True)),
                ('projectStatus', models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed')], max_length=100)),
                ('assignToPM', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_to_pm', to=settings.AUTH_USER_MODEL)),
                ('projectCreator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocation_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True)),
                ('taskName', models.CharField(max_length=100, null=True)),
                ('taskDescription', models.CharField(max_length=500, null=True)),
                ('taskStartDate', models.DateField(null=True)),
                ('taskEndDate', models.DateField(null=True)),
                ('taskStatus', models.BooleanField(default=False, null=True)),
                ('emp_allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.project')),
            ],
        ),
    ]
