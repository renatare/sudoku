import logging

logger =logging.getLogger(__name__)
logger_file = logging.FileHandler('execution_time.log')
logger.addHandler(logger_file)
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s')
logger_file.setFormatter(logger_formatter)

# logging.basicConfig( 
#     level=logging.INFO, 
#     filename='execution_time2.log', 
#     format='%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s'
# )

streamer_handler = logging.StreamHandler()
streamer_handler.setFormatter(logger_formatter)
logger.addHandler(streamer_handler)
