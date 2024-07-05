from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ["slug"]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
