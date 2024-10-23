import logging
import os
from datetime import datetime

# Creating log file name with timestamp format "MM_DD_YYYY_HH_MM_SS.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Defining the directory where logs will be stored
logs_path = os.path.join(os.getcwd(), "logs")

# Creating the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Defining the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring logging with the specified settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Logging file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log format
    level=logging.INFO,  # Setting the logging level to INFO
)


