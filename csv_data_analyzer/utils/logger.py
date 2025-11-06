# this is logger.py
import logging 
import os 

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'csv_analyzers.log')

logging.basicConfig(
    filename= LOG_FILE,
    level= logging.INFO,
    format=  '%(asctime)s | %(levelname)s | %(message)s',
    datefmt= "%Y %m %d, %H:%M:%S"
)

logs = logging.getLogger(__name__)