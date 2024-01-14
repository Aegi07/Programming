import logging
import datetime as dt

today = dt.datetime.today()
file_name = f'{today.year}-{today.month:02d}-{today.day:02d}.log'
# debug <- sees everything
# info
# warning
# error
# critical <- sees only critical

logging.basicConfig(level=logging.DEBUG) # sometimes this isnt enough to set the config of logging level
##  this solves the problem above
# for handler in logging.root.handlers: 
#     logging.root.removeHandler(handler)

# logging.log(logging.DEBUG, "First Logging Message")
# logging.log(logging.INFO, "First Logging Message")
# logging.log(logging.WARNING, "First Logging Message")
# logging.log(logging.ERROR, "First Logging Message")
# logging.log(logging.CRITICAL, "First Logging Message")

# logging.debug('second message')
# logging.info('second message')
# logging.warning('second message')
# logging.error('second message')
# logging.critical('second message')


logger = logging.getLogger('MYLOGGER')


file_handler = logging.FileHandler(f'Python/output/{file_name}')
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.critical('some info')