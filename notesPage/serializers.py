from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    attachment_url = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = [
            'id', 'title', 'description',
            'attachment', 'attachment_url',
            'views_count', 'created_at', 'updated_at',
            'owner'
        ]
        read_only_fields = ['owner', 'views_count', 'created_at', 'updated_at']

    def get_attachment_url(self, obj):
        if obj.attachment:
            return self.context['request'].build_absolute_uri(obj.attachment.url)
        return None
