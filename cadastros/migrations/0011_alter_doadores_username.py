# Generated by Django 3.2.8 on 2021-11-16 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0010_alter_doadores_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doadores',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user', unique=True),
            preserve_default=False,
        ),
    ]