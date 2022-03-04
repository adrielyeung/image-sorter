# image-sorter
A Python UI to enable automation of sorting **Camera Upload** photos and videos by date, place, category.

## Getting started
### Prerequisites
Require OpenCV Python, PyQt5 for core functions.

### Installing
After cloning the repository, run ```application.py```.

## User guide
### Browse mode
The GUI starts up in the **Browse mode**. Click "Browse" to browse for a directory to process images. If you have a path, you may input in Folder Path Input before clicking.

<img src="https://github.com/adrielyeung/image-sorter/blob/main/img/GUIBrowse.png" alt="Image Sorter GUI Browse mode" width="70%" height="70%">

### Image view mode
After browsing for a directory, all images and videos prefixed "IMG_", "VID_" and "PANO_" respectively
(normally default file names by Camera Upload) are sorted into folders according to their shot date.
(e.g. an image with path "dir/IMG_abc.png" shot at 4/Mar/2022 will be sorted into "dir/20220304" folder.)

For each date folder, all images within are displayed in the **Image view mode** in thumbnail display (for videos, first frame is taken).
Here you may change the number of images per row, border width between images, sort images according to file name, file size etc.
Double-click on any image to zoom in.

<img src="https://github.com/adrielyeung/image-sorter/blob/main/img/GUIImageView.png" alt="Image Sorter GUI Image view mode" width="70%" height="70%">
<img src="https://github.com/adrielyeung/image-sorter/blob/main/img/GUIZoom.png" alt="Image Sorter GUI Zoom in mode" width="70%" height="70%">

After viewing, select a category from dropdown or enter a new category (e.g. a place / food / activity etc.). Then click "Submit" when done.

This process repeats until all date folder are categorised. The GUI will return to Browse mode when done, with a "<Finish>" message.

<img src="https://github.com/adrielyeung/image-sorter/blob/main/img/GUIFinish.png" alt="Image Sorter GUI Finish message" width="70%" height="70%">

## Program flow and main files
The program flow is outlined as in below diagram:

<img src="https://github.com/adrielyeung/image-sorter/blob/main/img/ImageSorterFlow.png" alt="Image Sorter Flow" width="80%" height="80%">

- ```application.py```: serves as entry point to the application, triggers GUI to start up.
- ```gui.py```: loads and wires up fields in ```res/imagesort.ui``` (you may use Qt Designer to modify its design). Main operation of sorting into folders,
loading images into UI and categorising are in this file.
- ```imageutil.py```: Utility functions for image files, using OpenCV package, e.g. load, combine, add padding, scale and display into QLabel.
- ```videoutil.py```: Utility functions for video files, using OpenCV package, for now, only get first frame as thumbnail function.
- ```sort_folder_by_date.py```: Sort images / videos / panoramic images prefixed "IMG_", "VID_" and "PANO_" respectively in selected directory / directories into dated folder.
- ```logsetup.py```: Set up root logger and sub-loggers. Logger hierarchy in this project is one sub-logger for gui and sort_folder_by_date under root logger.
All sub-logger messages are routed to root logger, and handled in ```log/yyyymmdd.log``` file.

### Future developments
1. Auto-identify category through computer vision (OpenCV).
  
Feel free to suggest!
