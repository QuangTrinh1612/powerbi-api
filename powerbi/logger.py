import os
import yaml
import logging.config

# Define path to the logging configuration file
LOG_CONFIG_FILE = os.getenv("LOG_CONFIG_FILE", "config\logging.yaml")

def setup_logging(config_file: str):
    """Set up logging using the specified YAML configuration file."""
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)
    else:
        raise FileNotFoundError(f"Logging configuration file {config_file} not found.")
    
def get_logger(name: str):
    setup_logging(LOG_CONFIG_FILE)
    
    """Retrieve a logger with the specified name."""
    return logging.getLogger(name)