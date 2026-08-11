from .models import Application, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']



class Applicationserializers(serializers.ModelSerializer):
    tags =TagSerializer(many = 'True')
    class Meta:
        model = Application
        fields = ['id', 'user', 'company', 'role', 'status',
            'applied_date', 'notes',
            'created_at', 'updated_at', 'tags']
        read_only_fields = [ 'created_at', 'updated_at']