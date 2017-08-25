#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, include
from rest_framework import routers

from views import HoneypotView

router = routers.SimpleRouter()

router.register(r"save_data", HoneypotView, base_name="honeypot")
urlpatterns = router.urls
