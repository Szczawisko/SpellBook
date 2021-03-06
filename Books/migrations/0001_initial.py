# Generated by Django 4.0.6 on 2022-07-12 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('realase_date', models.DateField()),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('FA', 'Fantasy'), ('HO', 'Horror'), ('CO', 'Comedy'), ('TH', 'Thriller')], max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.author')),
            ],
        ),
    ]
