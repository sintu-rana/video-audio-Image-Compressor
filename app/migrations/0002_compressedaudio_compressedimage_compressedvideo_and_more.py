# Generated by Django 4.2.5 on 2023-09-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompressedAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='compressed_audio/')),
            ],
        ),
        migrations.CreateModel(
            name='CompressedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='compressed_images/')),
            ],
        ),
        migrations.CreateModel(
            name='CompressedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to='compressed_videos/')),
            ],
        ),
        migrations.DeleteModel(
            name='SaveFile',
        ),
    ]