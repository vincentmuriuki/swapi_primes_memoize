from .models import FavCharacter
from rest_framework import serializers

class FavCharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavCharacter
        fields = '__all__'
