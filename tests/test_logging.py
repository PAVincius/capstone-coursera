import os
import sys
import shutil
import pytest
from src.logger import get_logger

def test_logging_directory():
    """
    Ensures that when running tests, logs are directed to logs/test/
    """
    # Force the module to think we are in pytest (which we are)
    # The logger logic checks 'pytest' in sys.modules
    
    # Clean up previous test logs
    log_dir = os.path.join("logs", "test")
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)
        
    logger = get_logger("TEST_LOGGER")
    logger.info("Test log message")
    
    # Check if directory exists
    assert os.path.exists(log_dir)
    assert os.path.exists(os.path.join(log_dir, "app.log"))
