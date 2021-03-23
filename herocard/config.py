import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "7c6e905c-f589-4037-ab6d-9a2e051b805b")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "4d4a4c6b-b0c7-45eb-b835-587215ca7429")
