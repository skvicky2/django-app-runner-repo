# Generated by Django 4.2.2 on 2024-03-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_metadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharevideo',
            options={'verbose_name': 'Shared Video', 'verbose_name_plural': 'Shared Videos'},
        ),
        migrations.AlterModelOptions(
            name='videometadata',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
        migrations.AddField(
            model_name='sharevideo',
            name='from_email',
            field=models.EmailField(default='', max_length=255, verbose_name='From Email'),
        ),
        migrations.AddField(
            model_name='sharevideo',
            name='from_name',
            field=models.CharField(default='', max_length=255, verbose_name='From Name'),
        ),
        migrations.AddField(
            model_name='sharevideo',
            name='to_name',
            field=models.CharField(default='', max_length=255, verbose_name='To Name'),
        ),
        migrations.AlterField(
            model_name='sharevideo',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='To Email'),
        ),
    ]
