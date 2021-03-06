# Generated by Django 2.1.7 on 2019-05-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=1500, verbose_name='Текст статьи')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('author', models.TextField(max_length=100, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'post',
                'ordering': ['create'],
            },
        ),
    ]
