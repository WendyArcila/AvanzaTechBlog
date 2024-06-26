from rest_framework import serializers
from comment.models import BlogComments
from rest_framework.exceptions import ValidationError
from blog_post.models import BlogPost


class CommentSerializer(serializers.ModelSerializer):
    
    author_name = serializers.CharField(source='author.nick_name', read_only=True)
    
    class Meta:
        model = BlogComments
        fields = ['author', 'author_name', 'blog_post', 'comment', 'created_date']
        read_only_fields = ['author', 'author_name', 'created_date']

    def validate_blog_post(self, value):
        try:
            BlogPost.objects.get(pk=value.id)
        except BlogPost.DoesNotExist:
            raise ValidationError("The specified post does not exist.")
        return value
