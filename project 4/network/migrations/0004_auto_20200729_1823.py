# Generated by Django 3.0.8 on 2020-07-29 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20200729_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.PositiveIntegerField(default=0)),
                ('following', models.ManyToManyField(blank=True, null=True, related_name='following_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
