# Generated by Django 4.2.4 on 2023-09-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registertion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='', max_length=20)),
                ('Lastname', models.CharField(default='', max_length=20)),
                ('Email', models.EmailField(default='', max_length=20)),
                ('Companyname', models.CharField(default='', max_length=20)),
                ('Companyurl', models.URLField(default='', max_length=20)),
                ('Companysize', models.CharField(default='', max_length=20)),
                ('Phone', models.IntegerField(default='')),
                ('organisation', models.CharField(default='', max_length=200)),
                ('comments', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
