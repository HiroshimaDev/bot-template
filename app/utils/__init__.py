from .log import Log

__log__ = Log()

def get_logger(name):
    return __log__.getLogger(name)