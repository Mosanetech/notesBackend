from rest_framework import serializers
from users.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
     username=serializers.CharField(source="user.username",read_only=True)
     full_name=serializers.SerializerMethodField()

     class Meta:
          model=Profile
          fields=['photo','username','full_name','bio']

     def get_full_name(self,obj):
          return f"{obj.user.first_name} {obj.user.last_name}".strip()    