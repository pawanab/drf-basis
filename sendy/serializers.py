from rest_framework import serializers
from sendy.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language',
                    'style', 'owner', 'url', 'highlight', 'owner_url']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'url']