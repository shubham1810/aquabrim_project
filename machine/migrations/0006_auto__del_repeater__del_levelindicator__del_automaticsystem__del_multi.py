# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Repeater'
        db.delete_table(u'machine_repeater')

        # Deleting model 'LevelIndicator'
        db.delete_table(u'machine_levelindicator')

        # Deleting model 'AutomaticSystem'
        db.delete_table(u'machine_automaticsystem')

        # Deleting model 'MultiTankOption'
        db.delete_table(u'machine_multitankoption')

        # Deleting model 'Device'
        db.delete_table(u'machine_device')

        # Adding model 'Transmitter'
        db.create_table(u'machine_transmitter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sub_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tank_75_full', self.gf('django.db.models.fields.BooleanField')()),
            ('tank_50_full', self.gf('django.db.models.fields.BooleanField')()),
            ('tank_25_full', self.gf('django.db.models.fields.BooleanField')()),
            ('flow_status', self.gf('django.db.models.fields.BooleanField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'machine', ['Transmitter'])

        # Adding model 'Controller'
        db.create_table(u'machine_controller', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('device_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('motor_status', self.gf('django.db.models.fields.BooleanField')()),
            ('signal_status', self.gf('django.db.models.fields.BooleanField')()),
            ('voltage', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['Controller'])

        # Deleting field 'Command.object_id'
        db.delete_column(u'machine_command', 'object_id')

        # Deleting field 'Command.content_type'
        db.delete_column(u'machine_command', 'content_type_id')

        # Deleting field 'Command.description'
        db.delete_column(u'machine_command', 'description')

        # Adding field 'Command.enabled'
        db.add_column(u'machine_command', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Repeater'
        db.create_table(u'machine_repeater', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('field_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['Repeater'])

        # Adding model 'LevelIndicator'
        db.create_table(u'machine_levelindicator', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('field_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['LevelIndicator'])

        # Adding model 'AutomaticSystem'
        db.create_table(u'machine_automaticsystem', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('field_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['AutomaticSystem'])

        # Adding model 'MultiTankOption'
        db.create_table(u'machine_multitankoption', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('field_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['MultiTankOption'])

        # Adding model 'Device'
        db.create_table(u'machine_device', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('field_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['Device'])

        # Deleting model 'Transmitter'
        db.delete_table(u'machine_transmitter')

        # Deleting model 'Controller'
        db.delete_table(u'machine_controller')

        # Adding field 'Command.object_id'
        db.add_column(u'machine_command', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=''),
                      keep_default=False)

        # Adding field 'Command.content_type'
        db.add_column(u'machine_command', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Adding field 'Command.description'
        db.add_column(u'machine_command', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Command.enabled'
        db.delete_column(u'machine_command', 'enabled')


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
        u'machine.command': {
            'Meta': {'object_name': 'Command'},
            'electronic_format': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'machine.controller': {
            'Meta': {'object_name': 'Controller'},
            'device_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motor_status': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signal_status': ('django.db.models.fields.BooleanField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'voltage': ('django.db.models.fields.IntegerField', [], {})
        },
        u'machine.transmitter': {
            'Meta': {'object_name': 'Transmitter'},
            'device_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'flow_status': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tank_25_full': ('django.db.models.fields.BooleanField', [], {}),
            'tank_50_full': ('django.db.models.fields.BooleanField', [], {}),
            'tank_75_full': ('django.db.models.fields.BooleanField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['machine']