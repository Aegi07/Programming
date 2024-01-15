import logging
import datetime as dt

def get_logger(log_level, log_name='MYLOGGER', log_path='Python/use_logger/logs'):
    
    levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    logging.basicConfig(level=levels[log_level])
    
    logger = logging.getLogger(log_name)

    today = dt.datetime.today()
    file_name = f'{today.year}-{today.month:02d}-{today.day:02d}.log'
    formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(f'{log_path}/{file_name}')
    file_handler.setLevel(levels[log_level])
    file_handler.setFormatter(formatter) 
    logger.addHandler(file_handler)
    return logger
