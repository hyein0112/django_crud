from rest_framework import serializers
from .models import Addresses

class AddressesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['id','name', 'phone_number', 'address']