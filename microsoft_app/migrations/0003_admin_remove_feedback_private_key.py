# Generated by Django 4.0.4 on 2022-04-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microsoft_app', '0002_feedback_private_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('private_key', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='private_key',
        ),
    ]