# Generated by Django 4.0.4 on 2022-05-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]
