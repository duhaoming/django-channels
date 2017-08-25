from django.test import TestCase

# Create your tests here.

import random
import socket
import struct
from geoip import geolite2

ip = socket.inet_ntoa(struct.pack(">I", random.randint(1, 0xffffffff)))
info = geolite2.lookup(ip)

print info.get_info_dict
