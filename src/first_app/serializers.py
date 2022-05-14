
from codecs import lookup_error
from re import I
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse
from . models import Contact, Agent, Home, Image_files

from . validators import validate_email  



class Contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'







class Agent_serializer(serializers.ModelSerializer):
    
    url = serializers.SerializerMethodField(read_only = True)# to have url 1st way 1



#****************** to have url best way******************
    edit_url = serializers.HyperlinkedIdentityField(  # to have url 2nd way 
        view_name= 'update',
        lookup_field = 'pk'
    )


    
    # # custom validation with serializer 2nd way. mostly 2nd one is used ******
    email = serializers.CharField(validators=[validate_email])
    

    class Meta:
        model = Agent
        fields = ['edit_url','url','id','name', 'biodata', 'email', 'phone', 'image', 'top_seller', 'date_hired']
    



#********************* to have url*********************************
    def get_url(self, obj): # to have url 1st way 2

        request = self.context.get('request') # we get what the url request

        if request is None:
            return None

        # here retrive-detail is url name from urls.py
        return reverse("retrive-detail", kwargs={"pk": obj.pk}, request=request)






    # # custom validation with serializer 1st way************************************
    # # def validate_fieldname(self, value):
    # def validate_email(self, value):


    #     # request = self.context.get('request')
    #     # user = request.user
    #     # print('user..........', user) #to have user


    #     print('value...', value) # will print the posted email

    #     # qs = Agent.objects.filter(fieldname__exact = value)
    #     qs = Agent.objects.filter(email__exact = value) # case sensitive
    #     # qs = Agent.objects.filter(email__iexact = value) # not case sensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already exists")
        
    #     return value
       



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
        
