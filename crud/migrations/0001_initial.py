# Generated by Django 3.2.16 on 2022-12-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ali', max_length=255, verbose_name='Ism')),
                ('l_name', models.CharField(help_text='Aliyev', max_length=255, verbose_name='Familya')),
                ('age', models.IntegerField(help_text='25', verbose_name='Yoshi')),
                ('country', models.CharField(help_text='China', max_length=255, verbose_name='Vatani')),
                ('region', models.CharField(help_text='Samarqand', max_length=255, verbose_name='Viloyat')),
                ('group', models.IntegerField(verbose_name='Guruh')),
            ],
        ),
    ]
