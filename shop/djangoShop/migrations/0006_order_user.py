# Generated by Django 2.2.2 on 2019-06-06 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangoShop', '0005_order_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
