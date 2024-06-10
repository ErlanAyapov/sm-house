import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import CommandSerializer
from .utils import send_message  # Импорт функции
 

class ControlLightAPIView(APIView):
    def post(self, request):
        serializer = CommandSerializer(data=request.data)
        if serializer.is_valid():
            command = serializer.validated_data['command']

            # Отправка сообщения с помощью функции send_message
            action = send_message(command)

            # Пример кода для включения/выключения лампочки
            if 'turn on' in action.lower():
                # Код для включения лампочки
                pass  # Замените на реальный код
            elif 'turn off' in action.lower():
                # Код для выключения лампочки
                pass  # Замените на реальный код

            return Response({'status': action})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
