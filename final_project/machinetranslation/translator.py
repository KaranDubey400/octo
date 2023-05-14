"""This module contains functions for translating text using IBM Watson Language Translator."""

import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


# Load environment variables
load_dotenv()

# Get API key and URL from environment variables
apikey = os.environ['API_KEY']
url = os.environ['API_URL']

# Create an instance of the Watson Language Translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate English to French using IBM Watson Language Translator API.

    Parameters:
    english_text (str): The English text to translate.

    Returns:
    str: The French translation of the input text.
    """

    # Return an empty string if input is null or empty
    if not english_text or not english_text.strip():
        return ""

    # Use Watson Language Translator API to translate English to French
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract the translated text from the JSON response
    french_text = translation['translations'][0]['translation']

    # Return the translated text
    return french_text


def french_to_english(french_text):
    """
    Translate French to English using IBM Watson Language Translator API.

    Parameters:
    french_text (str): The French text to translate.

    Returns:
    str: The English translation of the input text.
    """
    if not french_text or not french_text.strip():
        return ""

    # Use Watson Language Translator API to translate French to English
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    # Extract the translated text from the JSON response
    english_text = translation['translations'][0]['translation']

    # Return the translated text
    return english_text
