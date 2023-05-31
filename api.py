from os import name, system
from uuid import uuid4

from httpx import Client


class StupidGPT:
    # Can't generate this chatbotid, otherwise you will get an error (No chatbot with ID: generated ID)
    CHATBOT_ID = 'd31c8fec-24fd-4a41-a9b9-1cb14565dbc1'

    @classmethod
    def send_message(cls, prompt: str):
        if not hasattr(cls, 'user_id'):
            cls.user_id = None

        if not hasattr(cls, 'conversation_id'):
            cls.conversation_id = None

        if not hasattr(cls, 'client'):
            cls.client = Client(timeout=30)
            cls.client.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
                'Content-Type': 'application/json',
                'Referer': f'https://ora.ai/embed/{cls.CHATBOT_ID}'
            })

        json_data = {
            'chatbotId': cls.CHATBOT_ID,
            'input': prompt,
            'userId': f'auto:{uuid4()}' if cls.user_id is None else cls.user_id,
            'provider': 'OPEN_AI',
            'config': False,
            'includeHistory': True,
        }

        if cls.conversation_id:
            json_data['conversationId'] = cls.conversation_id

        response = cls.client.post('https://ora.ai/api/conversation', json=json_data)
        content = response.json()
        result = content.get('response')

        if result is None:
            raise ValueError('Failed to get a response, please try again!')

        cls.conversation_id = content.get('conversationId')
        cls.user_id = content.get('userId')

        return result

    @classmethod
    def close_session(cls):
        if hasattr(cls, 'client'):
            cls.client.close()

    @staticmethod
    def get_query(prompt: str):
        print(prompt, end='')
        return '\n'.join(iter(input, ''))

    @staticmethod
    def clean_console():
        system('cls' if name == 'nt' else 'clear')
