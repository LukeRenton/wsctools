from bs4 import BeautifulSoup
import googletrans
from langdetect import detect
from wsctools.wslogging import wsLogger

class wsTranslator():
    def __init__(self, verbose: bool = False, logger: wsLogger = None):
        """
        Initializes a new instance of the `wsTranslator` class.

        Parameters:
        - `verbose` (bool, optional): If `True`, enables verbose mode for logging (default is `False`).
        - `logger` (wsLogger, optional): An instance of the `wsLogger` class for handling logging (default is `None`).

        Returns:
        - `wsTranslator`: An instance of the `wsTranslator` class.
        """
        self.Logger = logger if logger else wsLogger(verbose)

    def detect_website_language(self, soup : BeautifulSoup): 
        """
        Detects the language of the website.

        Parameters:
        - `soup` (BeautifulSoup): The BeautifulSoup object of the website.

        Returns:
        - `str`: The detected website language according to [googletrans.LANGUAGES](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages) short form.
        """
        
        self.Logger.log("Detecting website language...")
        website_language = ""
        try:
            website_language = soup.html.attrs['lang']
        except:
            self.Logger.log("Could not immediately detect language, using deep search")
            

        if not (website_language in googletrans.LANGUAGES):
                website_language = website_language.split("-")[0]
                if not (website_language in googletrans.LANGUAGES):
                    try:
                        self.Logger.log("We could not detect the language of the website: trying to detect using langdetect")
                        website_language = detect(soup.text)
                        self.Logger.log("Detected website language is: " + website_language)
                    except:
                        self.Logger.log("Exception occured deafulting trying to detect the website language: defaulting to english")
                        website_language = 'en'
                    if not (website_language in googletrans.LANGUAGES):
                        self.Logger.log("We could not detect the language of the website: defaulting to english")
                        website_language = 'en'
        self.Logger.log("Detected website language is: " + googletrans.LANGUAGES[website_language])
        return website_language
    
if __name__ == "__main__":
    import requests
    translator = wsTranslator(verbose=True)
    resposne = requests.get("https://www.pyamg.org/category/slot-indonesia/")
    soup = BeautifulSoup(resposne.text, 'html.parser')

    translator.detect_website_language(soup)