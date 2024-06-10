import  os
import requests
from django.conf import settings

def send_message(message): 
    api_key = settings.OPENAI_API_KEY
    print(api_key)
    if api_key is None:
        raise ValueError("The OPENAI_API_KEY environment variable is not set")

    # URL для обращения к OpenAI API
    url = "https://api.openai.com/v1/chat/completions"

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"  
    }

    # Данные запроса
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Ты используешься для как асистент для умного дома. Ты умеешь включить и выключить свет дома. Если пользователь будет спросить включить то должен отправить 1 если выключить то 0."},
            {"role": "user", "content": message}
        ]
    }

    # Отправка POST-запроса к API
    response = requests.post(url, headers=headers, json=data)

    # Проверка ответа и вывод результата
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"
