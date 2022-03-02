# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore

def getImage(image_filename):
    return cv2.imread(image_filename)

def combineImages(img_all, borderWidth, winWidth, numImage):
    # Width / height of each image
    boxWidth = int(winWidth / numImage) - (2 * borderWidth)

    # Calculate the new sizes of the images after resizing by ratio
    for i in range(len(img_all)):
        if img_all[i].shape[1] < img_all[i].shape[0]:  # width < height
            dsize = (int((img_all[i].shape[1] / img_all[i].shape[0] * boxWidth)), boxWidth)
            img_all[i] = cv2.resize(img_all[i], dsize, None, 0, 0, cv2.INTER_AREA)
            pad_area = boxWidth - dsize[0]
            # Pad the image to fit thumbnail and add extra border
            if pad_area % 2 == 0:  # even number of pixels
                img_all[i] = cv2.copyMakeBorder(img_all[i], borderWidth, borderWidth,
                                                     borderWidth + pad_area // 2,
                                                     borderWidth + pad_area // 2,
                                                     cv2.BORDER_CONSTANT, value=(255, 255, 255))
            else:  # odd number of pixels
                img_all[i] = cv2.copyMakeBorder(img_all[i], borderWidth, borderWidth,
                                                     borderWidth + (pad_area - 1) // 2,
                                                     borderWidth + (pad_area + 1) // 2,
                                                     cv2.BORDER_CONSTANT, value=(255, 255, 255))
            # white borders on four sides with left/right padding
        elif img_all[i].shape[1] == img_all[i].shape[0]:  # width = height
            dsize = (boxWidth, boxWidth)
            img_all[i] = cv2.resize(img_all[i], dsize, None, 0, 0, cv2.INTER_AREA)
            img_all[i] = cv2.copyMakeBorder(img_all[i], borderWidth, borderWidth,
                                                 borderWidth, borderWidth, cv2.BORDER_CONSTANT,
                                                 value=(255, 255, 255))
            # just border, no padding
        else:  # width > height
            dsize = (boxWidth, int((img_all[i].shape[0] / img_all[i].shape[1] * boxWidth)))
            img_all[i] = cv2.resize(img_all[i], dsize, None, 0, 0, cv2.INTER_AREA)
            pad_area = boxWidth - dsize[1]
            if pad_area % 2 == 0:  # even number of pixels
                img_all[i] = cv2.copyMakeBorder(img_all[i], borderWidth + pad_area // 2,
                                                     borderWidth + pad_area // 2, borderWidth,
                                                     borderWidth, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            else:  # odd number of pixels
                img_all[i] = cv2.copyMakeBorder(img_all[i], borderWidth + (pad_area - 1) // 2,
                                                     borderWidth + (pad_area + 1) // 2, borderWidth,
                                                     borderWidth, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            # border with top/bottom padding
    img_stack_h = [img_all[0].copy()]

    level = 0
    i = 1

    # Stack horizontally
    while i < len(img_all):
        if img_stack_h[level].shape[1] + img_all[i].shape[1] > winWidth:  # change to next row
            if (i + 1 < len(img_all) and
                img_all[i].shape[1] + img_all[i + 1].shape[1] > winWidth) \
                    or (i == len(img_all) - 1):
                # pads the end of the row or pads after the last picture
                finalpad = winWidth - img_all[i].shape[1]
                img_end = cv2.copyMakeBorder(img_all[i], 0, 0, 0, finalpad, cv2.BORDER_CONSTANT,
                                             value=(255, 255, 255))
                img_stack_h.append(img_end)
            else:
                img_stack_h.append(img_all[i])
            level += 1

        else:  # stack on same row
            if (i + 1 < len(img_all) and img_stack_h[level].shape[1] + img_all[i].shape[1]
                    + img_all[i + 1].shape[1] > winWidth) \
                    or (i == len(img_all) - 1):
                # pads the end of the row or pads after the last picture
                finalpad = winWidth - img_stack_h[level].shape[1] - img_all[i].shape[1]
                img_end = cv2.copyMakeBorder(img_all[i], 0, 0, 0, finalpad, cv2.BORDER_CONSTANT,
                                             value=(255, 255, 255))
                img_stack_h[level] = np.concatenate((img_stack_h[level], img_end), axis=1)
            else:
                img_stack_h[level] = np.concatenate((img_stack_h[level], img_all[i]), axis=1)
        i += 1
    comb_image = img_stack_h[0].copy()

    # Stack vertically
    for lev in range(1, len(img_stack_h)):
        comb_image = np.concatenate((comb_image, img_stack_h[lev]), axis=0)

    return comb_image, img_all, boxWidth

def displayImage(image, imageQLabel):
    # Setting image format based on loaded data
    # Default single channel image in grayscale with 8-bit depth
    qformat = QImage.Format_Indexed8

    # 3 dimensions with "channels" input
    if len(image.shape) == 3:  # rows [0], cols [1], channels [2]
        if (image.shape[2]) == 4:  # 4 channels with alpha channel (transparency)
            qformat = QImage.Format_RGBA8888
        else:
            qformat = QImage.Format_RGB888

    # OpenCV image, width, height, stride (width + additional padding pixels), qformat
    img = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)

    # BGR (OpenCV) --> RGB (QImage)
    img = img.rgbSwapped()
    # Set the pixel map
    imageQLabel.setPixmap(QPixmap.fromImage(img))
    # Aligning the image
    imageQLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
    
def scaleImage(img_enlarge, winHeight, winWidth):
    # Scaling the image to fit into the screen
    if img_enlarge.shape[1] < img_enlarge.shape[0]:  # width < height
        dsize = (int((img_enlarge.shape[1] / img_enlarge.shape[0] * winHeight)),
                 winHeight)
        img_enlarge = cv2.resize(img_enlarge, dsize, None, 0, 0, cv2.INTER_AREA)
        pad_area = winHeight - dsize[1]
        pad_width = winWidth - dsize[0]
        
        if pad_area > 0:
            if pad_area % 2 == 0:
                pad_area_l = pad_area // 2
                pad_area_r = pad_area // 2
            else:
                pad_area_l = (pad_area - 1) // 2
                pad_area_r = (pad_area + 1) // 2
        else:
            pad_area_l = 0
            pad_area_r = 0
        if pad_width > 0:
            if pad_width % 2 == 0:
                pad_width_l = pad_width // 2
                pad_width_r = pad_width // 2
            else:
                pad_width_l = (pad_width - 1) // 2
                pad_width_r = (pad_width + 1) // 2
        else:
            pad_width_l = 0
            pad_width_r = 0
        return cv2.copyMakeBorder(img_enlarge, pad_area_l, pad_area_r, pad_width_l,
                                              pad_width_r, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        # left/right padding
    elif img_enlarge.shape[1] == img_enlarge.shape[0]:  # width = height
        dsize = (winHeight, winHeight)
        img_enlarge = cv2.resize(img_enlarge, dsize, None, 0, 0, cv2.INTER_AREA)
        pad_area = winHeight - dsize[1]
        pad_width = winWidth - dsize[0]
        if pad_area > 0:
            if pad_area % 2 == 0:
                pad_area_l = pad_area // 2
                pad_area_r = pad_area // 2
            else:
                pad_area_l = (pad_area - 1) // 2
                pad_area_r = (pad_area + 1) // 2
        else:
            pad_area_l = 0
            pad_area_r = 0
        if pad_width > 0:
            if pad_width % 2 == 0:
                pad_width_l = pad_width // 2
                pad_width_r = pad_width // 2
            else:
                pad_width_l = (pad_width - 1) // 2
                pad_width_r = (pad_width + 1) // 2
        else:
            pad_width_l = 0
            pad_width_r = 0
        return cv2.copyMakeBorder(img_enlarge, pad_area_l, pad_area_r, pad_width_l,
                                              pad_width_r, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        # padding on four sides to fit into the rectangular display area
    else:  # width > height
        dsize = (winWidth, int((img_enlarge.shape[0] / img_enlarge.shape[1]
                                    * winWidth)))
        img_enlarge = cv2.resize(img_enlarge, dsize, None, 0, 0, cv2.INTER_AREA)
        pad_area = winHeight - dsize[1]
        pad_width = winWidth - dsize[0]
        if pad_area > 0:
            if pad_area % 2 == 0:
                pad_area_l = pad_area // 2
                pad_area_r = pad_area // 2
            else:
                pad_area_l = (pad_area - 1) // 2
                pad_area_r = (pad_area + 1) // 2
        else:
            pad_area_l = 0
            pad_area_r = 0
        if pad_width > 0:
            if pad_width % 2 == 0:
                pad_width_l = pad_width // 2
                pad_width_r = pad_width // 2
            else:
                pad_width_l = (pad_width - 1) // 2
                pad_width_r = (pad_width + 1) // 2
        else:
            pad_width_l = 0
            pad_width_r = 0
        return cv2.copyMakeBorder(img_enlarge, pad_area_l, pad_area_r, pad_width_l,
                                              pad_width_r, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        # padding on four sides to fit into the rectangular display area
        
def getClearPixmap(image):
    '''
    Generate a transparent pixel map, used to clear any image.

    Parameters
    ----------
    image : QLabel which holds the image

    Returns
    -------
    clrPixmap : QPixmap
        Transparent QPixmap with same height and width of image.

    '''
    clrPixmap = QPixmap(image.frameGeometry().width(), image.frameGeometry().height())
    clrPixmap.fill(QtCore.Qt.transparent)
    return clrPixmap
