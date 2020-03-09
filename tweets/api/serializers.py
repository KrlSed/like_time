from rest_framework import serializers

from likes import services as likes_services
from ..models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = (
            'id',
            'body',
            'total_likes'
        )
    
    def get_is_fan(self,obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fun(obj, user)
    