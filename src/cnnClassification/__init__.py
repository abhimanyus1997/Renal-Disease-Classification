import os
import sys
import logging

# Define the log format
logging_string = "[%(asctime)s] : [%(levelname)s] - %(message)s"

# Set up a log directory and file
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir, "running_logs.log")

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,
    format=logging_string,
    handlers=[
        # FileHandler: Logs will be written to a file (running_logs.log).
        logging.FileHandler(log_filepath),

        # StreamHandler: Logs will be displayed on the console.
        logging.StreamHandler(sys.stdout)
    ]
)

# Get a logger instance
logger = logging.getLogger("cnnClassificationLogger")
