import os
import sys
import logging

# Logging configuration
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Create a custom logger
logger = logging.getLogger("textSummarizerLogger")
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler(log_filepath)
console_handler = logging.StreamHandler(sys.stdout)

# Set format for handlers
formatter = logging.Formatter(logging_str)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
