# Generated by Django 2.0.2 on 2019-03-05 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NLP_MAPS',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('Address', models.TextField()),
                ('intensity', models.IntegerField()),
                ('Remarks', models.CharField(default='Road Block', max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(default='NITK Rescue Team', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]