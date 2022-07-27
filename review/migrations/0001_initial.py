# Generated by Django 4.0.6 on 2022-07-27 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('reviews', models.TextField()),
                ('spoilers', models.BooleanField(default=False)),
                ('recomendation', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='movie.movie')),
            ],
        ),
    ]