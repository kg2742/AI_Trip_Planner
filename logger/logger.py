import logging
import os

# Determine the root directory (assumes this file is in a subfolder)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, 'app.log')

def get_logger(name: str = 'app'):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(ch)
    return logger

# Example usage:
# logger = get_logger(__name__)
# logger.info("Logger initialized.")
def main():
    test_logger = get_logger(__name__)
    test_logger.debug('debug message')
    test_logger.info('info message')
    test_logger.warning('warn message')
    test_logger.error('error message')
    test_logger.critical('critical message')
    
if __name__ == '__main__':
    main()