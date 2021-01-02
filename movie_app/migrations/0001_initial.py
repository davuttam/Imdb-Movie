# Generated by Django 3.1.4 on 2021-01-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('slug', models.SlugField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=55)),
                ('imdb_score', models.FloatField()),
                ('popularity', models.FloatField()),
                ('genre', models.ManyToManyField(related_name='movies', to='movie_app.Genre')),
            ],
        ),
    ]