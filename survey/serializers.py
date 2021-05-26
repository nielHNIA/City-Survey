from rest_framework import serializers

from survey.models import City, State




class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            '__all__'
        )
