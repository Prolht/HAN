# Generated by Django 3.0.1 on 2020-01-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanzi', '0006_auto_20191230_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinesecharacters',
            name='img_file',
            field=models.ImageField(blank=True, default='', upload_to='cha/', verbose_name='存储位置'),
        ),
    ]
