# Generated by Django 4.1.4 on 2022-12-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_alter_order_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='upload',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
