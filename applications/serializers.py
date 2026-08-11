from .models import Application, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']



class Applicationserializers(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    
    tag_ids =serializers.PrimaryKeyRelatedField(many =True,source='tags',write_only=True, queryset=Tag.objects.all())
    class Meta:
        model = Application
        fields = ['id', 'user', 'company', 'role', 'status',
            'applied_date', 'notes',
            'created_at', 'updated_at', 'tags','tag_ids']
        read_only_fields = [ 'created_at', 'updated_at']


