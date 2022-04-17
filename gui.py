# -*- coding: utf-8 -*-
import sys
import os
import re
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication, QLabel
from PyQt5.uic import loadUi
from natsort import natsorted

import logsetup
import sort_folder_by_date as sf
import videoutil as vu
import imageutil as iu

guilogger = logsetup.setup(__file__)

# Log msg
START_SORT_FOLDER_BY_DATE = 'Start call sort_folder_by_date, directory {dirname}'
END_SORT_FOLDER_BY_DATE = 'End call sort_folder_by_date, directory {dirname}. Number of files sorted: {filecount}'
DISPLAY_FOLDER = 'Start display folder {dirname}'
NAME_FOLDER = 'Folder {dirname} named as category {cate}'
FINISHED_FOLDER = 'Finished categorising directory {dirname}'
FINISHED_GUI = '<Finished>'
NO_IMAGE_FOUND = '<No image or video found in above directory>'

# File extensions
JPG_EXT = '.jpg'
PNG_EXT = '.png'
MP4_EXT = '.mp4'

class ExtendedQLabel(QLabel):
    '''
    Extended QLabel which extracts the x- and y-position of user click,
    for providing further action.
    '''
    clicked = pyqtSignal(str)

    def __init__(self, parent):
        super(ExtendedQLabel, self).__init__(parent)
        self.pos_x = None
        self.pos_y = None

    def mouseDoubleClickEvent(self, QMouseEvent):
        # Extract x- and y-positions of mouse double click
        self.pos_x = QMouseEvent.x()
        self.pos_y = QMouseEvent.y()

class ResizableQDialog(QDialog):
    resized = pyqtSignal()

    def __init__(self):
        super(ResizableQDialog, self).__init__()

    def resizeEvent(self, event):
        # Emit signal when resized (to connect to the function which resizes the widgets)
        self.resized.emit()

class GUI(ResizableQDialog):
    def __init__(self):
        super(GUI, self).__init__()
        # Loads the UI
        loadUi('res/imagesort.ui', self)
        
        self.initAll()
        
    def initAll(self):        
        self.initVariables()
        self.initWindowProperties()
        self.initButtonActions()
        
    def initVariables(self):
        self.dirPath = None
        self.datePath = None
        self.image = None
        self.imgEnlarge = None
        # img_all stores the images with padding
        self.img_all = []
        # img_original stores the images without padding (as loaded)
        self.img_original = []
        # fnames stores all file attributes of each loaded file in tuples
        self.fnames = []
        # dnames stores all date directories names (yyyymmdd)
        self.dnames = []
        # cnames stores all sorted categories' names (e.g. places / food etc.)
        self.cnames = ['']
        # dind is the index of current iteration of dnames
        self.dind = 0
        self.boxWidth = None
        self.borderWidth = None
        self.imgIndex = None
    
    def initWindowProperties(self):
        # Set minimise / maximise buttons
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinMaxButtonsHint)
        # Setup the image display within the scrollable area
        self.displayArea.setWidgetResizable(True)
        self.imgLabel = ExtendedQLabel(self)
        self.displayArea.setWidget(self.imgLabel)
        # Width and height of the display box
        self.winWidth = self.displayArea.frameGeometry().width() - 20  # - 20 to account for the scroll bar
        self.winHeight = self.displayArea.frameGeometry().height() - 10
        # Setup the number of image per row input (spin) box
        self.numImageInput.setValue(5)
        self.numImageInput.setRange(1, 10)
        self.numImageInput.setSingleStep(1)
        self.borderInput.setValue(5)
        self.borderInput.setRange(0, 10)
        self.borderInput.setSingleStep(1)
        # Clear all available categories
        self.availCategoryBox.clear()
    
    def initButtonActions(self):
        # Use the "clicked.connect" to connect each action (clicked, changed values) to the call function (slot),
        # using the name defined in Designer.
        self.numImageInput.valueChanged.connect(self.on_spinbox_valueChanged)
        self.borderInput.valueChanged.connect(self.on_spinbox_valueChanged)
        self.browseButton.clicked.connect(self.browseClicked)
        self.imgLabel.mouseDoubleClickEvent = self.enlarge
        self.zoomOutButton.clicked.connect(self.zoomOutClicked)
        self.refreshButton.clicked.connect(self.load)
        self.submitButton.clicked.connect(self.submitCategory)
        # Zoom out button only clickable after enlarging an image
        self.zoomOutButton.setEnabled(False)
        # Resizing window connects to function to change widget sizes
        self.resized.connect(self.resizeWidget)
        # Enable browsing but diable all other functions
        self.enableBrowse(True)
    
    # The slot is a callable function which an action performed by the user will connect to.
    @pyqtSlot()
    def browseClicked(self):
        '''
        Function when "Browse" button clicked.
        Generates an input box for user to select folder path to sort images in.
        
        '''
        # Use ".text()" to extract the text input
        if self.inputPathEdit.text() == "":
            initPath = "C:\\Users"
        else:
            initPath = self.inputPathEdit.text()

        # QFileDialog is the dialog box to browse the directories
        # Arguments (self, window_name, initial_path)
        directory = QFileDialog.getExistingDirectory(self, "Browse Folder", initPath)

        if directory:
            # Sort into directory with date
            self.dirPath = directory
            if self.sortDirectoryByDate() > 0:
                self.loadDateDirectories()
                # Disable browsing and enable zoom in, submit etc.
                self.enableBrowse(False)
            else:
                self.dateLabel.setText(NO_IMAGE_FOUND)
            self.inputPathEdit.setText(directory)
            
    def sortDirectoryByDate(self):
        '''
        Calls sort_folder_by_date.sort_directory_by_date method to sort all images
        and videos into folder named as date (i.e. yyyymmdd)

        '''
        guilogger.info(START_SORT_FOLDER_BY_DATE.format(dirname=self.dirPath))
        os.chdir(self.dirPath)
        filecount = sf.sort_directory_by_date(self.dirPath)
        guilogger.info(END_SORT_FOLDER_BY_DATE.format(dirname=self.dirPath, filecount=filecount))
        return filecount
    
    def loadDAndCnames(self, conly=False):
        for (dirpath, dirnames, filenames) in os.walk(self.dirPath):
            for dirname in dirnames:
                if re.search("^[0-9]+$", dirname):
                    if not conly:
                        self.dnames.append(dirname)
                else:
                    self.cnames.append(dirname)
            break
    
    def loadDateDirectories(self):
        self.loadDAndCnames()        
        self.availCategoryBox.addItems(self.cnames)
        self.loadNextDateDirectory()
    
    def loadNextDateDirectory(self):
        # Finish processing all directories
        if self.dind >= len(self.dnames):
            self.clearImage()
            self.dateLabel.setText(FINISHED_GUI)
            self.initAll()
            self.enableBrowse(True)
            guilogger.info(FINISHED_FOLDER.format(dirname=self.dirPath))
        # Only work with date folders (yyyymmdd)
        else:
            dname = self.dnames[self.dind]
            self.dind += 1
            self.datePath = os.path.join(self.dirPath, dname)
            guilogger.info(DISPLAY_FOLDER.format(dirname=self.datePath))
            self.loadPath(os.listdir(self.datePath))
            self.load()
            self.dateLabel.setText(dname)
        self.categoryEdit.setText('')
    
    def clearImage(self):
        self.imgLabel.setPixmap(iu.getClearPixmap(self.imgLabel))
    
    @pyqtSlot()
    def submitCategory(self):
        # Validate user has non-space input
        category = self.categoryEdit.text().strip()
        if len(category) == 0:
            category = str(self.availCategoryBox.currentText()).strip();
            
        if len(category) > 0:
            tpath = os.path.join(self.dirPath, category)
            
            if not os.path.isdir(tpath):
                os.mkdir(tpath)
            
            # Move each file into specified category folder
            for fname in os.listdir(self.datePath):
                os.replace(os.path.join(self.datePath, fname), os.path.join(tpath, fname))
            
            # Refresh available categories if new category
            if not category in self.cnames:
                self.loadDAndCnames(True)
                self.availCategoryBox.clear()
                self.availCategoryBox.addItems(self.cnames)
            
            # If date folder empty, remove
            if not os.listdir(self.datePath):
                os.rmdir(self.datePath)
            
            guilogger.info(NAME_FOLDER.format(dirname=self.dateLabel.text(), cate=category))
            self.loadNextDateDirectory()

    def loadPath(self, list_of_fnames):
        '''
        Add file name (path), last modification time, creation time and file size
        of loaded files as tuples into self.fnames

        Parameters
        ----------
        list_of_fnames : list

        '''
        os.chdir(self.datePath)
        self.fnames = []
        for fname in list_of_fnames:
            # Only load specified image and video formats
            if fname.endswith(PNG_EXT) or fname.endswith(JPG_EXT) or \
                fname.endswith(MP4_EXT):
                self.fnames.append([fname, os.path.getmtime(fname), 
                                    os.path.getctime(fname), os.path.getsize(fname)])
        os.chdir(self.dirPath)
    
    @pyqtSlot()
    def load(self):
        if self.fnames:
            self.sortFiles()
            self.readFiles()
            self.combineImages()
            self.displayImage(self.image)

    def sortFiles(self):
        '''
        Sorts images according to radio button chosen
        (file name / mod date / create date / file size).

        '''
        # Sorting
        if self.sortDescendRadio.isChecked():
            reverse = True
        else:
            reverse = False
            self.sortAscendRadio.setChecked(True)
        # Check sorting parameter
        if self.sortFileNameRadio.isChecked():
            # Sort English filenames
            self.fnames = natsorted(self.fnames, key=lambda files: files[0], reverse=reverse)
        elif self.sortModDateRadio.isChecked():
            self.fnames = sorted(self.fnames, key=lambda files: files[1], reverse=reverse)
        elif self.sortCreateDateRadio.isChecked():
            self.fnames = sorted(self.fnames, key=lambda files: files[2], reverse=reverse)
        elif self.sortFileSizeRadio.isChecked():
            self.fnames = sorted(self.fnames, key=lambda files: files[3], reverse=reverse)

    def readFiles(self):
        '''
        Reads all files and combines them into one large image.

        '''
        os.chdir(self.datePath)
        self.img_original = []
        for name in self.fnames:
            img = None
            if name[0].endswith(MP4_EXT):
                img = vu.getFirstFrame(name[0])
            else:
                img = iu.getImage(name[0])
            # Save the original pictures when padding (border width / no. of images per row) changes
            self.img_original.append(img)
        
        os.chdir(self.dirPath)

    def combineImages(self):
        # Width of border - input
        self.borderWidth = self.borderInput.value()
        self.image, self.img_all, self.boxWidth = \
            iu.combineImages(self.img_original.copy(), self.borderWidth, 
                             self.winWidth, self.numImageInput.value())

    def displayImage(self, image):
        iu.displayImage(image, self.imgLabel)

    @pyqtSlot()
    def resizeWidget(self):
        '''
        Resize widgets and images (both thumbnails and zoomed) according to window size.

        '''
        # Width and height of the display box
        self.winWidth = self.displayArea.frameGeometry().width() - 20  # - 20 to account for the scroll bar
        self.winHeight = self.displayArea.frameGeometry().height() - 10
        if self.fnames:
            if self.imgIndex is not None:
                # In zoom mode
                self.imgEnlarge = iu.scaleImage(self.img_original[self.imgIndex].copy(), 
                                                 self.winHeight, self.winWidth)
                self.displayImage(self.imgEnlarge)
            else:
                # Not in zoom mode, call functions to regenerate the thumbnails
                self.combineImages()
                self.displayImage(self.image)

    @pyqtSlot(int)
    def on_spinbox_valueChanged(self, i):
        '''
        Function called when num of image displayed/border width spinboxes changed.
        Recalculates image position with updated values.

        Parameters
        ----------
        i : int
            Value in spinbox.

        '''
        # Recalculates values
        if self.img_all:
            self.combineImages()
            self.displayImage(self.image)

    @pyqtSlot()
    def enlarge(self, event):
        '''
        Function called when user double clicks on imgLabel.
        Calculates image to display in large size by position clicked,
        disables all inputs and buttons except "Zoom out"

        Parameters
        ----------
        event : Mouse click event
        
        '''
        # First check whether user double-clicks on a proper image. If yes then show a zoomed in image.
        if self.img_all:
            # Taking x- and y-positions of the double click to find out which image is being clicked on
            self.imgLabel.pos_x = event.x()
            self.imgLabel.pos_y = event.y()
            # Locate the row and column of the image
            row = self.imgLabel.pos_y//(self.boxWidth + 2*self.borderWidth)
            column = self.imgLabel.pos_x//(self.boxWidth + 2*self.borderWidth)
            self.imgIndex = row*self.numImageInput.value() + column
            if self.imgIndex < len(self.img_all):  # An image clicked, enter zoom mode
                self.enableZoomOut(False)
                self.imgEnlarge = iu.scaleImage(self.img_original[self.imgIndex].copy(), 
                                                 self.winHeight, self.winWidth)
                self.displayImage(self.imgEnlarge)

    @pyqtSlot()
    def zoomOutClicked(self):
        '''
        Function called when "Zoom out" button clicked, return to Thumbnail view.
        Enables all buttons except zoomOutButton.
        
        '''
        if self.img_all:
            self.displayImage(self.image)
            self.imgIndex = None
            self.imgEnlarge = None
            self.enableZoomOut(True)
            self.resizeWidget()
            
    def enableBrowse(self, enabled):
        '''
        Toggle enable between browse mode (browse for folder) and
        sort mode (sort each folder date into category after browsing for folder)

        Parameters
        ----------
        enabled : bool
            Browse mode enabled (True) or Sort mode enabled (False).

        '''
        self.inputPathEdit.setEnabled(enabled)
        self.browseButton.setEnabled(enabled)
        self.zoomOutButton.setEnabled(not enabled)
        self.numImageInput.setEnabled(not enabled)
        self.borderInput.setEnabled(not enabled)
        self.sortByBox.setEnabled(not enabled)
        self.sortBox.setEnabled(not enabled)
        self.refreshButton.setEnabled(not enabled)
        self.availCategoryBox.setEnabled(not enabled)
        self.categoryEdit.setEnabled(not enabled)
        self.submitButton.setEnabled(not enabled)

    def enableZoomOut(self, zoomOut):
        '''
        In zoom mode, enable "Zoom out",
        disable "Browse", sorting and clicking on the image display (imgLabel)

        Parameters
        ----------
        zoomOut : bool
            Whether to zoom out (True) or zoom in (False).

        '''
        if zoomOut:
            self.imgLabel.mouseDoubleClickEvent = self.enlarge
        else:
            self.imgLabel.mouseDoubleClickEvent = None
        
        self.zoomOutButton.setEnabled(not zoomOut)
        self.numImageInput.setEnabled(zoomOut)
        self.borderInput.setEnabled(zoomOut)
        self.sortByBox.setEnabled(zoomOut)
        self.sortBox.setEnabled(zoomOut)
        self.refreshButton.setEnabled(zoomOut)
        self.availCategoryBox.setEnabled(zoomOut)
        self.categoryEdit.setEnabled(zoomOut)
        self.submitButton.setEnabled(zoomOut)
        
def main():
    # Create application object
    app = QApplication(sys.argv)
    # Create GUI object
    window = GUI()
    # Set the title
    window.setWindowTitle("View Images")
    # Set the position and size of the dialog box (x-pos, y-pos, width, height)
    # window.setGeometry(0, 100, 400, 200)
    window.show()
    # Execute the application
    sys.exit(app.exec_())
