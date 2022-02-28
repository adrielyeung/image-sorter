# -*- coding: utf-8 -*-
import cv2

def get_first_frame(video_filename):
    '''
    Extract first frame image from a video file.

    Parameters
    ----------
    video_filename : str
        Path of video file.

    Returns
    -------
    image : numpy array
        First frame of video.

    '''
    cap = cv2.VideoCapture(video_filename)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    if cap.isOpened() and video_length > 0:
        success, image = cap.read()
        if success:
            return image
    return None
