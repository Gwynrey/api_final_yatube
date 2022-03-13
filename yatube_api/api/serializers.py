from django.contrib.auth import get_user_model
from rest_framework import serializers


from posts.models import Comment, Post, Group, Follow


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug', 'description',)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('user', 'following',)
        model = Follow

    def validate(self, data):
        following_request_value = data.get('following')
        request_user = self.context.get('request').user
        subscription_in_db_exists = Follow.objects.filter(
            user=request_user, following=following_request_value).exists()

        if following_request_value == request_user:
            raise serializers.ValidationError(
                'Невозможно подписаться на себя')
        elif subscription_in_db_exists:
            raise serializers.ValidationError(
                'Невозможно подписаться дважды')
        return data


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ['post']
        model = Comment
