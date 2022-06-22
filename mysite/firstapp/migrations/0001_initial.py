# Generated by Django 3.2.6 on 2021-08-25 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('Ma_so', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('url', models.URLField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.category')),
            ],
        ),
    ]