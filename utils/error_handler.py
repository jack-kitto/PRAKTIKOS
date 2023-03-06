import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)

    def log_error(self, error_message):
        self.logger.error(error_message)
