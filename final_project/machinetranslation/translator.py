'''
Translator Module with functions for French and English translations.
'''

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def translateToFrench(englishText):
    '''
    Function to convert english text to french text.
    '''
    fr_translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = fr_translation.get("translations")[0].get("translation")
    return frenchText


def translateToEnglish(frenchText):
    '''
    Function to convert french text to english text.
    '''
    en_translation = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = en_translation.get("translations")[0].get("translation")
    return englishText
