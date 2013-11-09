import datetime
from flask import url_for
from tracker import db

class Student(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    student_name = db.StringField(max_length=255, required=True)
    student_number = db.IntField(required=True) 
    slug = db.StringField(max_length=255, required=True)
    sessions = db.ListField(db.EmbeddedDocumentField('Session'))

    def get_absolute_url(self):
        return url_for('student', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.student_name

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class Session(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    student_number = db.IntField(required=True)
    subject = db.ListField(db.EmbeddedDocumentField('Subject'))
    score = db.DecimalField(required=True)

class Subject(db.EmbeddedDocument):
    title = db.StringField(max_length=255, required=True)

'''
class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)
    '''