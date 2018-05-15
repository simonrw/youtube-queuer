from __future__ import print_function, division, absolute_import
import logging


logging.basicConfig(level=logging.WARNING)

def create_logger(name):
    return logging.getLogger(name)


def set_verbosity(logger, verbose_count):
    if verbose_count is None:
        return

    if verbose_count == 1:
        logger.setLevel(logging.INFO)
    elif verbose_count > 1:
        logger.setLevel(logging.DEBUG)
