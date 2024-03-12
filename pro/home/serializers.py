from rest_framework import  serializers

from .models import Person,Color

class Colorserializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=['color_name','id']
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'


    def validate(self, data):
        if 'age' in data:
            if data['age']<18:
                raise serializers.ValidationError('age must be above 18')
        return data