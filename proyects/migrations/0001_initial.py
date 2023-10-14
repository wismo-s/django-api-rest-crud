# Generated by Django 4.2.6 on 2023-10-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]