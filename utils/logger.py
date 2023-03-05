# This file contains logging and debugging functionality for the RPA bot, 
# allowing developers to track the execution of the flow and identify 
# any errors or issues that may arise.

import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename='rpa-bot.log', level=logging.DEBUG)

    def log_debug(self, message):
        logging.debug(message)

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

    def log_critical(self, message):
        logging.critical(message)
