# Enhanced and Sophisticated Logging Epic

## Introduction

The "Enhanced and Sophisticated Logging" epic focuses on improving the logging capabilities of Praktikos. The goal is to provide developers with more detailed and actionable information about errors and system events. This will help developers quickly diagnose and resolve issues, leading to faster development cycles and better software quality.

## Classes

### ExceptionHandler

The `ExceptionHandler` class is responsible for catching and handling exceptions in Praktikos. It provides methods for logging exceptions and sending notifications to developers.

#### Methods

- `log_exception(exception: Exception) -> None`: Logs an exception to the error log.
- `send_notification(exception: Exception) -> None`: Sends a notification to developers about the exception.

#### Properties

- `error_logger: ErrorLogger`: The error logger used by the exception handler.

### ErrorLogger

The `ErrorLogger` class is responsible for logging errors in Praktikos. It provides methods for logging errors to different destinations such as the console, file, or database.

#### Methods

- `log_error(error: Error) -> None`: Logs an error to the error log.
- `get_errors() -> List[Error]`: Gets all errors from the error log.

#### Properties

- `log_file_path: str`: The file path of the error log.

### Error

The `Error` class represents an error in Praktikos. It contains information such as the error message, timestamp, and stack trace.

#### Properties

- `message: str`: The error message.
- `timestamp: datetime`: The timestamp of when the error occurred.
- `stack_trace: str`: The stack trace of the error.

### LogMessage

The `LogMessage` class represents a log message in Praktikos. It contains information such as the message, timestamp, and log level.

#### Properties

- `message: str`: The log message.
- `timestamp: datetime`: The timestamp of when the log message was created.
- `log_level: str`: The log level of the log message.

### Logger

The `Logger` class is responsible for logging messages in Praktikos. It provides methods for logging messages to different destinations such as the console, file, or database.

#### Methods

- `log_message(message: str, log_level: str) -> None`: Logs a message to the log.
- `get_messages(log_level: str) -> List[LogMessage]`: Gets all log messages from the log with the specified log level.

#### Properties

- `log_file_path: str`: The file path of the log.

## Files and Folders

- `logs/`: The folder that contains the log files.
- `errors/`: The folder that contains the error log files.
- `logger.py`: The file that contains the `Logger` class.
- `error_logger.py`: The file that contains the `ErrorLogger` class.
- `exception_handler.py`: The file that contains the `ExceptionHandler` class.

## Infrastructure

- The `logging` module in Python is used for logging messages to different destinations.
- The `smtplib` module in Python is used for sending email notifications.

## Educational Resources

- Python Logging HOWTO: https://docs.python.org/3/howto/logging.html
- Logging in Python - The Ultimate Guide: https://www.loggly.com/ultimate-guide/python-logging-basics/
- Python SMTP Documentation: https://docs.python.org/3/library/smtplib.html
