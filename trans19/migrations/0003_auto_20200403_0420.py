# Generated by Django 3.0.3 on 2020-04-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans19', '0002_auto_20200403_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id_number',
            field=models.CharField(help_text='Identity Document Number', max_length=10, verbose_name='ID Number'),
        ),
    ]