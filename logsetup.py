# -*- coding: utf-8 -*-
import os
import logging
import datetime as dt

DT_FORMATTER = '%Y%m%d'

# Log file and dir
LOG_FOLDER = 'log'
LOG_FNAME = LOG_FOLDER + os.sep + dt.datetime.now().strftime(DT_FORMATTER) \
    + '.log'

def setup(fullpath):
    '''
    Set up logger for file with path fullpath and all messages sent to file LOG_FNAME.

    Parameters
    ----------
    fullpath : str
        Full path of script file, extracting file name as logger name. The default is None (root logger).

    Returns
    -------
    Logger object created.

    '''
    file_name = os.path.basename(fullpath)
    if file_name.rfind('.') >= 0:
        file_name = file_name[:file_name.rfind('.')]
    return setupName(file_name)

def setupName(name=None):
    '''
    Set up logger with name and all messages sent to file LOG_FNAME.

    Parameters
    ----------
    name : str, optional
        Name of logger. The default is None (root logger).

    Returns
    -------
    Logger object created.

    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Clear all handlers
    if logger.hasHandlers():
        logger.handlers.clear()
    # Only add file handler for root logger
    # All sub-level loggers' messages will be passed to root logger's file handler
    if name is None:
        os.makedirs(LOG_FOLDER, exist_ok=True)
        filehandler = logging.FileHandler(LOG_FNAME)
        filehandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
    return logger
