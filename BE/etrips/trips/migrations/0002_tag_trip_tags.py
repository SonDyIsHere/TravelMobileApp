# Generated by Django 4.2.11 on 2024-04-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='trips.tag'),
        ),
    ]
