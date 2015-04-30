# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import media_tree.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('media_tree', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaTreeImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('link_type', models.CharField(default=None, choices=[(b'P', 'Link to page'), (b'U', 'Link to web address'), (b'I', 'Link to image detail'), (b'R', 'Link to URL pattern')], max_length=1, blank=True, help_text='Makes the image a clickable link.', null=True, verbose_name='link type')),
                ('link_url', models.CharField(help_text='For link to web address. Example: Enter "http://www.domain.com" to create an absolute link to an external site, or enter a relative URL like "/about/contact".', max_length=255, null=True, verbose_name='web address', blank=True)),
                ('link_target', models.CharField(blank=True, max_length=64, null=True, verbose_name='link target', choices=[(b'', 'same window'), (b'_blank', 'new window')])),
                ('width', media_tree.fields.DimensionField(help_text='You can leave this empty to use an automatically determined image width.', max_length=8, null=True, verbose_name='max. width', blank=True)),
                ('height', media_tree.fields.DimensionField(help_text='You can leave this empty to use an automatically determined image height.', max_length=8, null=True, verbose_name='max. height', blank=True)),
                ('render_template', models.CharField(help_text='Template used to render the image.', max_length=100, null=True, verbose_name='template', blank=True)),
                ('link_page', models.ForeignKey(blank=True, to='cms.Page', help_text='For link to page. Select any page from the list.', null=True, verbose_name='page')),
                ('node', media_tree.fields.FileNodeForeignKey(None, (241,), None, '\xa0\xa0\xa0', verbose_name='file', to='media_tree.FileNode')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
