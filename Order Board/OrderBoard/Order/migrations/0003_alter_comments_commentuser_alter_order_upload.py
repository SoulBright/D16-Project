# Generated by Django 4.1.4 on 2022-12-23 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order', '0002_alter_order_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='upload',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
