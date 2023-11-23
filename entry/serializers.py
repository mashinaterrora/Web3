from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('login', 'email', 'password', 'creation_date', 'id', 'otp')
