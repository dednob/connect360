from rest_framework import serializers

from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'story', 'blog_image', 'banner_image','slug']
