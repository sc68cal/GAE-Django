# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange db. order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the db. but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from google.appengine.ext import db

class WarDiary(db.Model):
    reportkey = db.StringProperty(multiline=True)
    date = db.TextProperty()
    type = db.StringProperty(multiline=True)
    category = db.StringProperty(multiline=True)
    trackingnumber = db.StringProperty(multiline=True)
    title = db.StringProperty(multiline=True)
    summary = db.TextProperty()
    region = db.StringProperty(multiline=True)
    attackon = db.StringProperty(multiline=True)
    complexattack = db.StringProperty(multiline=True)
    reportingunit = db.StringProperty(multiline=True)
    unitname = db.StringProperty(multiline=True)
    typeofunit = db.StringProperty(multiline=True)
    friendlywia = db.StringProperty(multiline=True)
    friendlykia = db.StringProperty(multiline=True)
    hostnationwia = db.StringProperty(multiline=True)
    hostnationkia = db.StringProperty(multiline=True)
    civilianwia = db.StringProperty(multiline=True)
    civiliankia = db.StringProperty(multiline=True)
    enemywia = db.StringProperty(multiline=True)
    enemykia = db.StringProperty(multiline=True)
    enemydetained = db.StringProperty(multiline=True)
    mgrs = db.StringProperty(multiline=True)
    latitude = db.StringProperty(multiline=True)
    longitude = db.StringProperty(multiline=True)
    originatorgroup = db.StringProperty(multiline=True)
    updatedbygroup = db.StringProperty(multiline=True)
    ccir = db.StringProperty(multiline=True)
    sigact = db.StringProperty(multiline=True)
    affiliation = db.StringProperty(multiline=True)
    dcolor = db.StringProperty(multiline=True)
    classification = db.StringProperty(multiline=True)

