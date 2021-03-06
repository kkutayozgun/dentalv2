# Generated by Django 3.2 on 2022-04-30 07:03

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_serviceitem_in_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitemtranslation',
            name='home_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Home Description'),
        ),
        migrations.AlterField(
            model_name='serviceitemtranslation',
            name='banner_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Banner Description'),
        ),
        migrations.AlterField(
            model_name='serviceitemtranslation',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content Body'),
        ),
    ]
