# -*- coding: utf-8 -*-
import cv2
import os

def main():
    folder_path = input("Enter folder path to create thumbnails in: ")
    genFirstFrameInFolder(folder_path)

def genFirstFrameInFolder(folder_path):
    for fname in os.listdir(folder_path):
        img_path = os.path.join(folder_path, os.path.splitext(fname)[0] + ".png")
        if fname.endswith(".mp4") and \
            not os.path.exists(img_path):
                success, encoded_img = \
                    cv2.imencode(".png", getFirstFrame(os.path.join(folder_path, fname)))
                with open(img_path, "wb") as img:
                    img.write(encoded_img)
                print("Successfully saved first frame of " + fname)

def getFirstFrame(video_filename):
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

if __name__ == '__main__':
    main()
