import requests
from decouple import config
from requests.api import head


class ContentModeratorApi:
    def __init__(self):
        self.TOKEN_CM = config("TOKEN_CM")

    def use_content_moderator(self, content):
        headers = {
            "Content-Type": "text/plain",
            "Ocp-Apim-Subscription-Key": self.TOKEN_CM,
        }
        response = requests.post(
            url="https://southcentralus.api.cognitive.microsoft.com/contentmoderator/moderate/v1.0/ProcessText/Screen?classify=True&language=por",
            data=content,
            headers=headers,
        )

        return response.json()
