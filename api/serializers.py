from rest_framework.serializers import ModelSerializer
from .models import Student


class studentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


def create(self, validate_data):
    return Student.objects.create(**validate_data)


def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.room)
    instance.roll = validated_data.get('roll', instance.roll)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance
