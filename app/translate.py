import json
import requests
from app import app

def translate(text, source_language, destination_language):
    if 'MS_TRANSLATION_KEY' not in app.config or not app.config['MS_TRANSLATION_KEY']:
        return "Error: translation service not configured."
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATION_KEY']}
    r = requests.get("https://google.com")
    if r.status_code != 200:
        return "Error: translation service failed"
    return "Success. Translated text here. Response code {}.".format(r.status_code)