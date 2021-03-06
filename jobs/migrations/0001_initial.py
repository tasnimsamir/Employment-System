# Generated by Django 4.0 on 2022-01-01 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('experience_level', models.CharField(choices=[('Junior', 'Junior'), ('Mid', 'Mid'), ('Senior', 'Senior')], max_length=15)),
                ('Programming_language', models.CharField(default='python', max_length=100)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(default='There is no Job description.', max_length=1000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('biography', models.TextField(max_length=1000)),
                ('Created_at', models.DateTimeField(auto_now=True)),
                ('experience_level', models.CharField(choices=[('Junior', 'Junior'), ('Mid', 'Mid'), ('Senior', 'Senior')], max_length=15)),
                ('Programming_language', models.CharField(default='python', max_length=100)),
                ('applied_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='jobs.job')),
            ],
        ),
    ]
