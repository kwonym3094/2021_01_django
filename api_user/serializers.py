from rest_framework import serializers
from .models import User

# response로 사용 될 data를 직렬화하여 json이나 xml등으로 손쉽게 변환이 가능함
# Django의 ORM을 이용하여 코드레벨에서 손쉽게 DB에 접근할 수 있음


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # 모델 User의 모든 field를 serializer함.
