# Generated by Django 3.1.3 on 2020-11-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCR712', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocr712',
            name='document',
            field=models.FileField(upload_to='documents/doc.pdf'),
        ),
    ]
