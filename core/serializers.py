from rest_framework import serializers
from django.conf import settings

from core.models import STKPushRequest


class STKPushSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)
    trans_ref = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = STKPushRequest
        fields = ['phone_number', 'amount', 'trans_ref', "description"]