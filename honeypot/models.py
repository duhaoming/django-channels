from __future__ import unicode_literals

import mongoengine
from mongoengine import signals

from django.db import models
from channels import Group
# Create your models here.

mongoengine.connect("test", host="127.0.0.1", username="duhaoming", password="shuaige")

class Session(mongoengine.Document):
    protocol = mongoengine.StringField(max_length=10, required=True)
    timestamp = mongoengine.DateTimeField(default="", required=True)
    source_ip = mongoengine.StringField(max_length=30, required=True)
    source_port = mongoengine.IntField(default="443", required=True)
    destination_port = mongoengine.IntField(default="443", required=True)
    identifier = mongoengine.StringField(max_length=50, required=True)
    honeypot = mongoengine.StringField(max_length=10, required=True)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        Group("chat-honeypot").send({'text': document.to_json()})

signals.pre_save.connect(Session.pre_save, sender=Session)
