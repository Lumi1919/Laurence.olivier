# Generated by Django 3.2.4 on 2022-05-31 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=233, null=True, upload_to=''),
        ),
    ]
