from rest_framework import serializers
from django.conf import settings

from core.models import STKPushRequest


class STKPushSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    amount = serializers.IntegerField()
    trans_ref = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = STKPushRequest
        fields = ['phone_number', 'amount', 'trans_ref', "description"]