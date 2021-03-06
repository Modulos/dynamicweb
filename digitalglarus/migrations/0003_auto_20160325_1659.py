# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('digitalglarus', '0002_auto_20160324_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dggallery',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='dggalleryplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='dggalleryplugin',
            name='dgGallery',
        ),
        migrations.RemoveField(
            model_name='dgpicture',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='dgpicture',
            name='image',
        ),
        migrations.RemoveField(
            model_name='dgsupportersplugin',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='Supporter',
        ),
        migrations.DeleteModel(
            name='DGGallery',
        ),
        migrations.DeleteModel(
            name='DGGalleryPlugin',
        ),
        migrations.DeleteModel(
            name='DGPicture',
        ),
        migrations.DeleteModel(
            name='DGSupportersPlugin',
        ),
    ]
