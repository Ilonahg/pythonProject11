from rest_framework import serializers

def validate_youtube_url(value):
    if 'youtube.com' not in value:
        raise serializers.ValidationError("Тільки посилання на youtube.com дозволені.")
    return value
