#!/usr/bin/python
#coding : utf-8

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from models import Session
from serializers import HoneypotSerializer


class HoneypotView(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = HoneypotSerializer

    @list_route()
    def save_session(self, request, pk=None):
        self.get_serializer_class().save()
        return Response({"message": "success"})

    @list_route()
    def get_data(self, request):
        data = self.get_queryset()
        serializers = HoneypotSerializer(data, many=True)
        return Response(serializers.data)
