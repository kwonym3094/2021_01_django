from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User

# Create your views here.
class UserView(APIView):

    """
    POST /user
    """

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)  # request의 데이터를 UserSerializer로 변환

        if user_serializer.is_valid():
            user_serializer.save()  # UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(
                user_serializer.data, status=status.HTTP_201_CREATED
            )  # client에게 JSON response 전달
        else:
            return Response(user_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    """
    GET /user
    GET /user/{user_id}
    """

    def get(self, request, **kwargs):
        if kwargs.get("user_id") is None:
            user_queryset = User.objects.all
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            user_id = kwargs.get("user_id")
            user_serializer = UserSerializer(User.objects.get(id=user_id))
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    """
    PUT /user/{user_id}
    """

    def put(self, request, **kwargs):
        if kwargs.get("user_id") is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get("user_id")
            user_object = User.objects.get(id=user_id)

            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    """
    DELETE /user/{user_id}
    """

    def delete(self, request, kwargs):
        if kwargs.get("user_id") is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get("user_id")
            user_object = User.objects.get(id=user_id)
            user_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)
