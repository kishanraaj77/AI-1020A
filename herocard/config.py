import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "053b477c-6f0b-4629-a12d-6bef846605ac")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "2da80739-ab3a-4fb1-8fa1-c4df64b087f2")
