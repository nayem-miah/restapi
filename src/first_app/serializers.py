
from rest_framework import serializers
from . models import Contact, Agent, Home, Image_files

class Contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class Agent_serializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class Home_serializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id','title','slug','photo','bedrooms','sqft','zipcode','address','city','sale_type','price')
        
class Home_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__' 
        lookup_field = 'slug'


class Image_files_serializer(serializers.ModelSerializer):
    class Meta:
        model = Image_files
        fields = '__all__' 
        
