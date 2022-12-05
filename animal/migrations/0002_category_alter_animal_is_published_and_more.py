# Generated by Django 4.1.3 on 2022-12-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография'),
        ),
        migrations.AddField(
            model_name='animal',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='animal.category', verbose_name='Категория'),
        ),
    ]
