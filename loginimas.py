import logging

logger =logging.getLogger(__name__)
logger_file = logging.FileHandler('logs.log')
logger.addHandler(logger_file)
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s')
logger_file.setFormatter(logger_formatter)

streamer_handler = logging.StreamHandler()
streamer_handler.setFormatter(logger_formatter)
logger.addHandler(streamer_handler)
