from rest_framework import serializers
from relation.models import Relation
from user.api.serialize import UsserSerializeLight

class RelationSeriazer(serializers.ModelSerializer):
    # from_user=serializers.CharField(source='from_user.username')
    from_user=UsserSerializeLight()
    follow_back=serializers.SerializerMethodField()

    class Meta:
        model=Relation
        fields=['from_user', 'to_user',"follow_back"]

    def get_follow_back(self,obj):
        return Relation.objects.filter(from_user=obj.to_user,to_user=obj.from_user).exists()


