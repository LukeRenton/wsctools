# WSCTools
## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Core Features](#core-features)
- [License](#license)

## About 
WSCTools is a collection of helper functions designed to facilitate efficient web scraping. This toolset provides utilities for handling headers, logging, URL translation and manipulation as well as many more functions to streamline the web scraping process. 

## Installation

To get started with WSCTools, you can install it via pip:

```bash
pip install wsctools==1.0.1
```

## Core Features

### 1. WSHeaders
Manage custom headers for web scraping requests.
```python
from wsctools.wsurls import wsHeaders
```

This module provides functions to manage and customize headers for web scraping requests. It helps in setting up the necessary headers to mimic browser requests and avoid detection.

- `get_pc_user_agent()`: Returns a randomly selected user agent string for a desktop browser.
- `get_mobile_user_agent()`: Returns a randomly selected user agent string for a mobile browser.

### 2. WSLogging
Implement logging to track web scraping activities and errors.
```python
from wsctools.wsurls import wsLogging
```

This module implements logging functionality to track the activities and errors encountered during web scraping. It ensures that all events are logged for later review and debugging. 

- `wsLogger(verbose=False)`: Initializes the logger with optional verbose mode.
- `log(message, force_verbose=False)`: Logs a message with the prefix "[LOG]".
- `info(message, force_verbose=False)`: Logs an information message with the prefix "[INFO]".
- `error(message, force_verbose=False)`: Logs an error message with the prefix "[ERROR]".

### Sample usage
The power in this module lies in that you can turn off all logging statements in one central file, while keeping statements you always want on by forcing it's verbosity as seen below. This is incredibly helpful for keeping debug statements and simply turning it off by changing one variable.

`Logger.py`
```python
from wsctools.wslogging import wsLogger

verbosity = False # This will change the verbosity across all files which imports Logger
logger = wsLogger(verbosity)
```

`OtherFile.py`
```python
from Logger import logger
logger.log("This message won't show up since verbosity is false in Logger.")
logger.log("This message will show up even though verbosity is false.", force_verbose=True)
```

### 3. WSTranslator
Translate web content if needed during scraping.
```python
from wsctools.wsurls import wsTranslator
```

The translator module provides functions to translate web content as needed. This can be particularly useful when scraping websites in different languages.

- `wsTranslator(verbose=False, logger=None)`: Initializes the translator with optional verbose mode and custom logger.
- `detect_website_language(soup)`: Detects the language of the website using a BeautifulSoup object.
- `contact_url_translation(website_language)`: Translates the word for "contact" based on the website language.

### 4. WSUrls
Handle and manipulate URLs for web scraping tasks.
```python
from wsctools.wsurls import wsUrls
```

This module contains utilities for handling and manipulating URLs, ensuring that all URLs are properly formatted and accessible during the web scraping process.

- `valid_url(url)`: Validates a given URL.
- `get_base_url(url)`: Gets the base URL of a given URL.
- `get_base_url_cache_safe(url)`: Gets the base URL of a given URL, cache safe.
- `standardize_url(url)`: Standardizes a given URL by adding the 'http://' prefix if missing.
- `is_relative_url(url)`: Checks if a given URL is relative.
- `is_contact_url(a_tag, base_url, word_for_contact)`: Checks if a given `<a>` tag represents a contact URL.
- `cloudflare_decrypt_mail(encrypted_mail)`: Decrypts a given Cloudflare encrypted mail.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/SomeFeature`)
3. Commit your changes (`git commit -m 'Added some feature'`)
4. Push to the branch (`git push origin feature/SomeFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.