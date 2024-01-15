from log_helper import get_logger


logger = get_logger(log_level=4)
logger.debug('debug message here')
logger.info('info message')
logger.warn('warn')
logger.error('error')
logger.critical('critical message')
logger.critical('-----end of log-----')


