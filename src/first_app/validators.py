
from first_app.models import Agent
from rest_framework import serializers

# custom validation with serializer 2nd way************************************
# def validate_fieldname(value):
def validate_email(value):
    print('value...', value) # will print the posted email
    # qs = Agent.objects.filter(fieldname__exact = value)
    qs = Agent.objects.filter(email__exact = value) # case sensitive
    # qs = Agent.objects.filter(email__iexact = value) # not case sensitive
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already exists")
    
    return value