from rest_framework import serializers
from users.models import CustomUser 

class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        identifier = data.get('identifier')
        password = data.get('password')

        if not identifier or not password:
            raise serializers.ValidationError("Both identifier and password are required.")

        user = None
        
        if "@" in identifier:
            try:
                user = CustomUser.objects.get(email=identifier)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("Invalid login credentials.")
        
        elif identifier.isdigit():
            try:
                user = CustomUser.objects.get(phone_number=identifier)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("Invalid login credentials.")

        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid login credentials.")

        data['user'] = user
        return data
