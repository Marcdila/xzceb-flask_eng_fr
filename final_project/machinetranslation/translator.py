"""
Features functions to do translation between english and french strings
"""

import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

VERSION = "2018-05-01"
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(url)

def translate_text(text, model_id):
    """
    Gets the best found translation for a text using the given model
    """

    # If the text is empty, return an empty text to avoid exception
    if text == "":
        return ""

    result = language_translator.translate(
        text=text,
        model_id=model_id,
    ).get_result()

    return result.get("translations")[0].get("translation")


def english_to_french(english_text):
    """
    Translates text from english to french
    """
    return translate_text(english_text, "en-fr")

def french_to_english(french_text):
    """
    Translates text from french to english
    """
    return translate_text(french_text, "fr-en")
