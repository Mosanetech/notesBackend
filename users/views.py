from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers.register_serializer import RegisterSerializer
from users.serializers.login_serializer import LoginSerializer
from users.models import CustomUser
#test
from rest_framework.views import APIView

class Helloworldview(APIView):
    def get(self,request):
        return Response({"message:":"helloworld"},status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number
        }, status=status.HTTP_200_OK)
