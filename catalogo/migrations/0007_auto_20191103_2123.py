# Generated by Django 2.2.6 on 2019-11-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20191103_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(default='static/img/mas.png', upload_to='NonEpicGames/catalogo/static/img'),
        ),
    ]