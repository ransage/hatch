# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entry.spec'
        db.delete_column(u'simplelist_entry', 'spec_id')

        # Adding field 'Entry.list'
        db.add_column(u'simplelist_entry', 'list',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['simplelist.List']),
                      keep_default=False)

        # Adding field 'Entry.create_date'
        db.add_column(u'simplelist_entry', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Entry.created_by'
        db.add_column(u'simplelist_entry', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'List.created_by'
        db.add_column(u'simplelist_list', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Entry.spec'
        raise RuntimeError("Cannot reverse this migration. 'Entry.spec' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Entry.spec'
        db.add_column(u'simplelist_entry', 'spec',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplelist.List']),
                      keep_default=False)

        # Deleting field 'Entry.list'
        db.delete_column(u'simplelist_entry', 'list_id')

        # Deleting field 'Entry.create_date'
        db.delete_column(u'simplelist_entry', 'create_date')

        # Deleting field 'Entry.created_by'
        db.delete_column(u'simplelist_entry', 'created_by_id')

        # Deleting field 'List.created_by'
        db.delete_column(u'simplelist_list', 'created_by_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simplelist.entry': {
            'Meta': {'object_name': 'Entry'},
            'body_text': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'doc_sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'heading_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplelist.List']"})
        },
        u'simplelist.list': {
            'Meta': {'object_name': 'List'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spec_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['simplelist']
