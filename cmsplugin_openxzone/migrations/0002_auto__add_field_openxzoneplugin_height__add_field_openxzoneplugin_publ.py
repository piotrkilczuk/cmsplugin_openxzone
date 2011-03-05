# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'OpenXZonePlugin.height'
        db.add_column('cmsplugin_openxzoneplugin', 'height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'OpenXZonePlugin.publisher_id'
        db.add_column('cmsplugin_openxzoneplugin', 'publisher_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'OpenXZonePlugin.tag'
        db.add_column('cmsplugin_openxzoneplugin', 'tag', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'OpenXZonePlugin.type'
        db.add_column('cmsplugin_openxzoneplugin', 'type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'OpenXZonePlugin.width'
        db.add_column('cmsplugin_openxzoneplugin', 'width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'OpenXZonePlugin.zone_name'
        db.add_column('cmsplugin_openxzoneplugin', 'zone_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'OpenXZonePlugin.height'
        db.delete_column('cmsplugin_openxzoneplugin', 'height')

        # Deleting field 'OpenXZonePlugin.publisher_id'
        db.delete_column('cmsplugin_openxzoneplugin', 'publisher_id')

        # Deleting field 'OpenXZonePlugin.tag'
        db.delete_column('cmsplugin_openxzoneplugin', 'tag')

        # Deleting field 'OpenXZonePlugin.type'
        db.delete_column('cmsplugin_openxzoneplugin', 'type')

        # Deleting field 'OpenXZonePlugin.width'
        db.delete_column('cmsplugin_openxzoneplugin', 'width')

        # Deleting field 'OpenXZonePlugin.zone_name'
        db.delete_column('cmsplugin_openxzoneplugin', 'zone_name')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_openxzone.openxzoneplugin': {
            'Meta': {'object_name': 'OpenXZonePlugin', 'db_table': "'cmsplugin_openxzoneplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'publisher_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'tag': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'zone_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'zone_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_openxzone']
