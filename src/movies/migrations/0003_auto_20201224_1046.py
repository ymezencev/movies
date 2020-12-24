# Generated by Django 3.1.4 on 2020-12-24 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201223_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie', verbose_name='фильм'),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='movies.review', verbose_name='Родитель'),
        ),
    ]