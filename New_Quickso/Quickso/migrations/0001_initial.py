# Generated by Django 4.1.7 on 2023-03-21 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='名称')),
                ('category', models.CharField(max_length=120, verbose_name='类别')),
                ('icon', models.CharField(max_length=64, verbose_name='图标')),
            ],
            options={
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('url', models.CharField(max_length=120, verbose_name='链接')),
                ('status', models.CharField(max_length=32, verbose_name='状态')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('category', models.CharField(default='None', max_length=120, verbose_name='类别')),
            ],
            options={
                'verbose_name_plural': '链接',
            },
        ),
    ]