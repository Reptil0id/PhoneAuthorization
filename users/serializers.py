from rest_framework import serializers

from .models import ReferralModel


class GetPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralModel
        fields = ('PhoneNumber',)


class ReferralCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralModel
        fields = ('PhoneNumber', 'Code')


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralModel
        fields = ('PhoneNumber',)