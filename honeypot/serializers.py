#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers

from models import Session

class HoneypotSerializer(serializers.Serializer):
    protocol = serializers.CharField(max_length=10)
    timestamp = serializers.DateTimeField()
    source_ip = serializers.CharField(max_length=30)
    source_port = serializers.IntegerField()
    destination_port = serializers.IntegerField()
    identifier = serializers.CharField(max_length=50)
    honeypot = serializers.CharField(max_length=10)

    def create(self, validated_data):
        session = Session(**validated_data)
        session.save()
        return session
