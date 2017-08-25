#!/usr/bin/env python
# encoding: utf-8

from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

@api_view(("GET",))
@permission_classes((AllowAny,))
def api_view(request, format=None):
    app_root = OrderedDict()
    app_root["honeypot"] = reverse("honeypot", request=request, format=format)
    return Response(app_root)
