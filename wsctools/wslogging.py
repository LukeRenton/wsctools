class wsLogger():
    def __init__(self, verbose=False):
        """
        A simple logging class for providing logs, information, error messages and more.

        Parameters:
        - `verbose` (bool, optional): If `True`, the logger will print output else not (default is `False`).
        """
        self.verbose = verbose
    
    def log(self, message, force_verbose=False):
        """
        Logs a message with the prefix "[LOG]" if verbose mode is enabled.

        Parameters:
        - `message` (str): The message to be logged.

        Example:
        ```
        logger.log("Processing the website...")
        ```
        >>> [LOG] Processing the website...
        """
        if self.verbose or (force_verbose == True):
            print("[LOG] " + message)
    
    def info(self, message, force_verbose=False):
        """
        Logs an information message with the prefix "[INFO]".

        Parameters:
        - `message` (str): The information message.

        Example:
        ```
        logger.info("Processing the website...")
        ```
        >>> [INFO] Processing the website...
        """
        if self.verbose or (force_verbose == True):
            print("[INFO] " + message)

    def error(self, message, force_verbose=False):
        """
        Logs an error message with the prefix "[ERROR]".

        Parameters:
        - `message` (str): The error message.

        Example:
        ```
        logger.error("An error occurred processing the website...")
        ```
        >>> [ERROR] An error occurred processing the website...
        """
        if self.verbose or (force_verbose == True):
            print("[ERROR] " + message)
        
        
