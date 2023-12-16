from rest_framework import serializers
from api.models import Job
from django.contrib.auth.models import User

# class JobSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)

#     def create(self, validated_data):
#         return Job.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

# class JobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Job
#         fields = ['id', 'name', 'owner']
#         owner = serializers.ReadOnlyField(source='owner.username')

# class UserSerializer(serializers.ModelSerializer):
#     jobs = serializers.PrimaryKeyRelatedField(many=True, queryset=Job.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'jobs']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class JobSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    # meta_name = serializers.HyperlinkedIdentityField(view_name='job-meta-name', format='html')

    class Meta:
        model = Job
        fields = ['name', 'id', 'description', 'meta_name', 'owner', 'full_name']
        # depth = 2