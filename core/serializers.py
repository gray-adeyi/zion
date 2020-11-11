from rest_framework import serializers
from .models import (
    Website,
    AdditionalInfo,
    FAQ,
    TeamMemberSocialAccount,
    TeamMember,
    Message,
)

class TeamMemberSocialAccountSerialzer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberSocialAccount
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    social_account = TeamMemberSocialAccountSerialzer(
        many = False, 
        required = True)

    class Meta:
        model = TeamMember
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'


class WebsiteSerializer(serializers.ModelSerializer):
    additional_info = AdditionalInfoSerializer(
        many = False, 
        read_only=True, 
        required=False)

    class Meta:
        model = Website
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'