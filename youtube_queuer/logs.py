from __future__ import print_function, division, absolute_import
import logging


logging.basicConfig(level=logging.DEBUG)

def create_logger(name):
    return logging.getLogger(name)
