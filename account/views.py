# обработчики запросов
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (RegistrationSerializer, ActivationSerializer, LoginSerializer,)
                          # ForgotPasswordSerializer, ForgotPasswordCompleteSerializer, ChangePasswordSerializer)


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Ваш аккаунт зарегистрирован. Чтобы активировать, введите код, отправленный Вам на почту',
                            status=201)
        return Response(serializer.errors, status=400)


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.activate()
            return Response('Аккаунт успешно активирован',
                            status=200)
        return Response(serializer.errors, status=400)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли с сайта')

# #1.
# class ForgotPasswordView(APIView):
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.send_new_pass()
#             return Response('Вам выслан новый пароль')
#         return Response(serializer.errors, status=400)

#
# # 2.
# class ForgotPasswordView(APIView):
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.send_code()
#             return Response('Вам вычлан код для восстановления пароля')
#         return Response(serializer.errors, status=400)
#
#
# class ForgotPasswordCompleteView(APIView):
#     def post(self, request):
#         serializer = ForgotPasswordCompleteSerializer(data=request.data)
#         if serializer.set_new_password():
#             serializer.set_new_password()
#         2mmgX7ys    return Response('Пароль успешно обнавлен')
#         return Response(serializer.errors, status=400)
#
#
# class ChangePasswordView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = ChangePasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.set_new_pass()
#             return Response('Вы успешно сменили пароль')
#         return Response(serializer.errors, status=400)
#
#
