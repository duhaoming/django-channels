#!/usr/bin/env python
# encoding: utf-8

from channels.routing import route
from consumers import  ws_connect, ws_disconnect, ws_keepalive, ws_message

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.keepalive", ws_keepalive),
    route("websocket.disconnect", ws_disconnect)
]
