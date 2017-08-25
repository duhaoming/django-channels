import json
import time

from channels import Group
from channels import Channel
from channels.sessions import channel_session
from django.dispatch import receiver
from django.db.models.signals import pre_save
#from channels.auth import channel_session_user_from_http
#from watchdog.observers.api import ObservedWatch
#from watchdog.observers import Observer

from models import Session

#class Message(object):
#    def __init__(self, message):
#        self.message = message
#
#    def dispatch(self, event):
#        method_map = {"modified": self.send_message}
#        event_type = event.event_type
#        if event_type == "modified":
#            method_map[event_type](event, self.message)
#
#    def send_message(self, event, message):
#        if message.channel_session['chat'] == 'ddos':
#            try:
#                with open(event.src_path, 'r') as f:
#                    Group("chat-%s" % message.channel_session['chat']).send({'text': f.read()})
#            except:
#                pass

@channel_session
def ws_connect(message):
    room = message.content['path'].strip("/")
    message.channel_session['chat'] = room
    Group("chat-%s" % room).add(message.reply_channel)

@channel_session
def ws_message(message, **kwargs):
    Group("chat-%s" % message.channel_session['chat']).send({'text': message.content["text"]})
#@channel_session
#def ws_message(message, **kwargs):
#    Group("chat-%s" % message.channel_session['chat']).send({"text": "nihao"})
#    if message.content['text'] == 'ni':
#        event_handler1 = Message(message)
#        observer = Observer()
#        watch = observer.schedule(event_handler1, path='/opt/signals', recursive=True)
#        #observer.add_handler_for_watch(event_handler1, watch)
#        observer.start()
#        try:
#            while 1:
#                time.sleep(1)
#        except KeyboardInterrupt:
#            observer.stop()
#        observer.join()

@channel_session
def ws_keepalive(message):
    Group("chat-%s" % message.channel_session['chat']).add(message.reply_channel)


@channel_session
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['chat']).discard(message.reply_channel)
