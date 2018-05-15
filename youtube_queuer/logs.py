import logging


logging.basicConfig(level=logging.DEBUG)

def create_logger(name):
    return logging.getLogger(name)
