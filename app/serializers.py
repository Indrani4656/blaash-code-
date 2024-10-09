from rest_framework import serializers

from app.models import *

class EngagementPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPost
        fields='_all_'
class EngagementPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPostContent
        fields='_all_'
class EngagementPostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPostProduct
        fields='_all_'
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields='_all_'


class EngagementPostCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPostCollection
        fields='_all_'