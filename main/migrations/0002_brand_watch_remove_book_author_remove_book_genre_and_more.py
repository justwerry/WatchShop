# Generated by Django 4.0.3 on 2022-03-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('date_of_found', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='brands')),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='watches')),
                ('status', models.CharField(choices=[('in stock', 'В наличии'), ('out of stock', 'Нет в наличии')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RenameModel(
            old_name='Genre',
            new_name='Model',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
