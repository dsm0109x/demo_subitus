# Generated by Django 2.2 on 2021-03-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210322_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_user_scorm',
            field=models.CharField(max_length=100, null=True, verbose_name='ID en SCORM'),
        ),
    ]