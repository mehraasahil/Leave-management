from rest_framework import serializers
from api.models import User,AddLeave,Empid
class UserSerializer(serializers.HyperlinkedModelSerializer):
    User_id=serializers.ReadOnlyField()
    class Meta:
        model = User
        fields='__all__'

class AddLeaveSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField
    class Meta:
        model = AddLeave
        fields='__all__'
class EmpidSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField
    class Meta:
        model = Empid
        fields='__all__'
