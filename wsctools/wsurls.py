from os import name
import tldextract
from urllib.parse import urlparse
from wsctools.wslogging import wsLogger

class wsUrls:
    def __init__(self, verbose: bool = False, logger: wsLogger = None):
        """
        Initializes a new instance of the `wsUrls` class.

        Parameters:
        - `verbose` (bool, optional): If `True`, enables verbose mode for logging (default is `False`).
        - `logger` (wsLogger, optional): An instance of the `wsLogger` class for handling logging (default is `None`).

        Returns:
        - `wsUrls`: An instance of the `wsUrls` class.
        """
        self.Logger = logger if logger else wsLogger(verbose)

    def valid_url(self, url ,verbose=True):
        """
        Validates a given URL.

        Parameters:
        - `url` (str): The URL to be validated.
        - `verbose` (bool, optional): If `True`, enables verbose mode for logging (default is `True`).

        Returns:
        - `bool`: `True` if the URL is valid, `False` otherwise.
        """

        if (verbose):
            self.Logger.log("Validating URL:  [" + url + "]")
        extracted_domain = tldextract.extract(url)
        return bool(extracted_domain.domain and extracted_domain.suffix)

    def get_base_url(self, url):
        """
        Gets the base URL of a given URL (Please don't use this if you are using multi-threading as tldextract is not thread safe and will cause you many headaches... trust me. Rather use get_base_url_cache_safe()).

        Parameters:
        - `url` (str): The URL to get the base URL from.

        Returns:
        - `str`: The base URL.
        """
        
        extracted_domain = tldextract.extract(url)
        return extracted_domain.registered_domain
    
    def get_base_url_cache_safe(self, url):
        """
        NOTE: Please only use this when you are using multi-threading (tldextract is not thread safe) otherwise use the tldextract method (get_base_url) as it is much more robust
        Gets the base URL of a given URL, we assume the URL is of the form (http(s)://)website.com.

        Parameters:
        - `url` (str): The URL to get the base URL from.

        Returns:
        - `str`: The base URL.
        """
        base_url = (url.replace("https://", "").replace("http://", "").replace("www.", "")).split("/")[0]
        return base_url

    def standardize_url(self, url):
        """
        Standardizes a given URL by adding the 'http://' prefix if missing.

        Parameters:
        - `url` (str): The URL to be standardized.

        Returns:
        - `str`: The standardized URL.
        """

        if (url.startswith("http://") == False) and (url.startswith("https://") == False):
            url = "http://" + url
        return url

    def is_relative_url(self, url):
        """
        Checks if a given URL is relative (e.g. /contact/).

        Parameters:
        - `url` (str): The URL to be checked.

        Returns:
        - `bool`: `True` if the URL is relative, `False` otherwise.
        """

        parsed_url = urlparse(url)
        return not parsed_url.scheme and not parsed_url.netloc

def base_url_test():
    with open("C:/Users/luker/OneDrive/Documents/Upwork work/wsctools/test files/baseline.csv", "r") as file:
        urls = wsUrls()
        for line in file:
            url = line.strip()
            tld_base_url = tldextract.extract(url).registered_domain
            my_base_url = urls.get_base_url(url)
            if (tld_base_url != my_base_url):
                print("Error: TLD base URL [" + tld_base_url + "] does not match my base URL [" + my_base_url + "] for URL [" + url + "]")
        

if __name__ == "__main__":
    ws_url = wsUrls()
    print(ws_url.get_base_url("https://www.ac.za.google.com?/w4920/---212304j21icwa'"))
    
        