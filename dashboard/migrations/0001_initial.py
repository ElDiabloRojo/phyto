# Generated by Django 3.0.3 on 2020-02-18 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunrise', models.DateField()),
                ('sunset', models.DateField()),
                ('feed', models.DateField()),
                ('plant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Plant')),
            ],
        ),
    ]
