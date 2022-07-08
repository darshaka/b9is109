# Generated by Django 4.0.3 on 2022-06-13 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='newspaper',
            name='newsAdmin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsInfo', models.TextField()),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.newspaper')),
            ],
        ),
        migrations.AddField(
            model_name='newspaper',
            name='newsTitle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.newstitle'),
        ),
    ]
