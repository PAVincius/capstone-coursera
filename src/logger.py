import logging
import os
import sys

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    console_handler.setFormatter(formatter)
    return console_handler

def get_file_handler(log_file):
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    file_handler.setFormatter(formatter)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG) # Better to have debug level for development

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(get_console_handler())
        
        # Determine log directory
        log_dir = "logs"
        if "pytest" in sys.modules:
             log_dir = os.path.join("logs", "test")
        
        os.makedirs(log_dir, exist_ok=True)
        logger.addHandler(get_file_handler(os.path.join(log_dir, "app.log")))

    # Check if a test is running and ensure logs go to logs/test if so. 
    # This is a fallback if the check above didn't catch specific test runners or if invoked differently.
    # However, reliance on sys.modules['pytest'] is a common heuristic.
    
    return logger
