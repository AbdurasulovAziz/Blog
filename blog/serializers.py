from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        obj = super(ArticleSerializer, self).to_representation(instance)
        obj['author'] = instance.author.user_name
        return obj
