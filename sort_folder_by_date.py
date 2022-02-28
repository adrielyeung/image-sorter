# -*- coding: utf-8 -*-
import sys, os
import datetime as dt
import PIL
import logsetup, logging

# Strings
IMAGE_PREFIX = 'IMG_'
PANO_PREFIX = 'PANO_'
VIDEO_PREFIX = 'VID_'
LINUX_SEP = '/'

# Formatter
DATE_FORMATTER = '%Y%m%d'

# Files
# __file__ contains full path of this script
FILE_NAME = os.path.basename(__file__)
if FILE_NAME.rfind('.') >= 0:
    FILE_NAME = FILE_NAME[:FILE_NAME.rfind('.')]

# Log msg
START_MOVE_FILE_MSG = 'Start cleaning directory {dirname}'
MOVED_FILE_MSG = 'Moved file {fname} into folder {dirname}'
END_MOVE_FILE_MSG = 'End cleaning directory {dirname}, ' \
    'num of files moved: {fcount}'

# sys.argv[0] contains running script full path (script that imported this)
APP_DIR = os.path.dirname(sys.argv[0])
DIRECTORY_FNAME = 'config' + os.sep + FILE_NAME + '_directory.txt'

# Logger for current file
sflogger = logsetup.setupName(FILE_NAME)

def main():
    directories = read_directories()
    
    for directory_str in directories:
        sflogger.info(START_MOVE_FILE_MSG.format(dirname = directory_str))
        try:
            filecount = sort_directory_by_date(directory_str)
            sflogger.info(END_MOVE_FILE_MSG.format(dirname=directory_str, fcount=filecount))
        except Exception:
            sflogger.exception(logging.formatException(sys.exc_info()))

def read_directories():
    with open(APP_DIR + os.sep + DIRECTORY_FNAME, 'r') as dirfile:
        lines = dirfile.readlines()
    return lines

def sort_directory_by_date(directory_str):
    '''
    Puts each image and video file in directory,
    prefixed with 'IMG_' and 'VID_',
    into folder named as image / video shoot date (yyyymmdd).
    Replaces the file in the destination folder if already exists.

    Parameters
    ----------
    directory_str : str
        Path of directory to process, in String format.

    '''
    directory = os.fsencode(directory_str)
    filecount = 0
    os.chdir(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith(IMAGE_PREFIX) or \
            filename.startswith(VIDEO_PREFIX) or \
                filename.startswith(PANO_PREFIX):
            mdate_str = "Undated"
            
            if filename.startswith(IMAGE_PREFIX) or \
                filename.startswith(PANO_PREFIX):
                mdate_str = getsdate(filename)
            
            if filename.startswith(VIDEO_PREFIX):
                mdate_str = getmdate(filename)
                
            # Move into folder named date (e.g. 20220222)
            if not os.path.isdir(mdate_str):
                os.mkdir(mdate_str)
            os.replace(filename, mdate_str + LINUX_SEP + filename)
            filecount += 1
            sflogger.info(MOVED_FILE_MSG.format(fname=filename, dirname=directory_str))
    return filecount

def getsdate(filename):
    '''
    Get photo shoot date for filename.

    Parameters
    ----------
    filename : str
        Image file name.

    Returns
    -------
    sdate : str
        Photo shoot date in yyyymmdd format.

    '''
    with PIL.Image.open(filename) as image:
        EXIF_data = image._getexif()
        sdate = EXIF_data.get(306)
    
    return sdate[0:4] + sdate[5:7] + sdate[8:10]

def getmdate(filename):
    '''
    Get file modified date for filename.

    Parameters
    ----------
    filename : str
        Image file name.

    Returns
    -------
    mdatetime_str : str
        File modified date in yyyymmdd format.

    '''
    mtime = os.path.getmtime(filename)
    mtimestamp = dt.datetime.fromtimestamp(mtime)
    mdatetime_str = mtimestamp.strftime(DATE_FORMATTER)
    return mdatetime_str
