from functools import wraps
from time import time
import logging


def log_timing(f):
    """
    Decorator which logs them execution time of a function.

    :param f: function
    :return: timed function
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        s = time()
        result = f(*args, **kwargs)
        logging.info('{} execution took {} seconds.'.format(f.__name__, time() - s))
        return result
    return wrapper