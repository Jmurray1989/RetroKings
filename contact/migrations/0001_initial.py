# Generated by Django 3.1.1 on 2020-10-08 19:01

import datetime
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
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact_date', models.DateTimeField(blank=True,
                                                      default=datetime.
                                                      datetime.now)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.
                                              db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
