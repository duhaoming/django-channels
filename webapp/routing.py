#!/usr/bin/env python
# encoding: utf-8

from channels.routing import route, include
from honeypot.routing import channel_routing as honeypot

channel_routing = [
    include(honeypot, path="/honeypot")
]
