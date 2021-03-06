# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Adriel\OneDrive\Documents\PythonScripts\ImageSorter\res\imagesort.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import gui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(910, 810))
        self.FullLayout = QtWidgets.QVBoxLayout(Dialog)
        self.FullLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.FullLayout.setObjectName("FullLayout")
        self.imgLayout = QtWidgets.QHBoxLayout()
        self.imgLayout.setObjectName("imgLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputLayout = QtWidgets.QVBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.inputPathLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.inputPathLabel.setFont(font)
        self.inputPathLabel.setObjectName("inputPathLabel")
        self.inputLayout.addWidget(self.inputPathLabel)
        self.inputPathEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.inputPathEdit.setFont(font)
        self.inputPathEdit.setObjectName("inputPathEdit")
        self.inputLayout.addWidget(self.inputPathEdit)
        self.horizontalLayout.addLayout(self.inputLayout)
        self.browseButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.numImageLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.numImageLabel.setFont(font)
        self.numImageLabel.setObjectName("numImageLabel")
        self.verticalLayout_2.addWidget(self.numImageLabel)
        self.numImageInput = QtWidgets.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.numImageInput.setFont(font)
        self.numImageInput.setMinimum(1)
        self.numImageInput.setMaximum(10)
        self.numImageInput.setProperty("value", 5)
        self.numImageInput.setObjectName("numImageInput")
        self.verticalLayout_2.addWidget(self.numImageInput)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.borderLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.borderLabel.setFont(font)
        self.borderLabel.setObjectName("borderLabel")
        self.verticalLayout_3.addWidget(self.borderLabel)
        self.borderInput = QtWidgets.QSpinBox(Dialog)
        self.borderInput.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.borderInput.setFont(font)
        self.borderInput.setMinimum(0)
        self.borderInput.setMaximum(10)
        self.borderInput.setProperty("value", 5)
        self.borderInput.setObjectName("borderInput")
        self.verticalLayout_3.addWidget(self.borderInput)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.imgLayout.addLayout(self.horizontalLayout_2)
        self.FullLayout.addLayout(self.imgLayout)
        self.sortLayout = QtWidgets.QHBoxLayout()
        self.sortLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.sortLayout.setObjectName("sortLayout")
        self.sortByBox = QtWidgets.QGroupBox(Dialog)
        self.sortByBox.setMinimumSize(QtCore.QSize(500, 56))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortByBox.setFont(font)
        self.sortByBox.setObjectName("sortByBox")
        self.sortFileNameRadio = QtWidgets.QRadioButton(self.sortByBox)
        self.sortFileNameRadio.setGeometry(QtCore.QRect(10, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortFileNameRadio.setFont(font)
        self.sortFileNameRadio.setChecked(False)
        self.sortFileNameRadio.setObjectName("sortFileNameRadio")
        self.sortNoRadio = QtWidgets.QRadioButton(self.sortByBox)
        self.sortNoRadio.setGeometry(QtCore.QRect(390, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortNoRadio.setFont(font)
        self.sortNoRadio.setChecked(True)
        self.sortNoRadio.setObjectName("sortNoRadio")
        self.sortModDateRadio = QtWidgets.QRadioButton(self.sortByBox)
        self.sortModDateRadio.setGeometry(QtCore.QRect(10, 50, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortModDateRadio.setFont(font)
        self.sortModDateRadio.setObjectName("sortModDateRadio")
        self.sortFileSizeRadio = QtWidgets.QRadioButton(self.sortByBox)
        self.sortFileSizeRadio.setGeometry(QtCore.QRect(200, 30, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortFileSizeRadio.setFont(font)
        self.sortFileSizeRadio.setObjectName("sortFileSizeRadio")
        self.sortCreateDateRadio = QtWidgets.QRadioButton(self.sortByBox)
        self.sortCreateDateRadio.setGeometry(QtCore.QRect(200, 50, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortCreateDateRadio.setFont(font)
        self.sortCreateDateRadio.setCheckable(True)
        self.sortCreateDateRadio.setChecked(False)
        self.sortCreateDateRadio.setObjectName("sortCreateDateRadio")
        self.sortLayout.addWidget(self.sortByBox)
        self.sortBox = QtWidgets.QGroupBox(Dialog)
        self.sortBox.setMinimumSize(QtCore.QSize(292, 56))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortBox.setFont(font)
        self.sortBox.setObjectName("sortBox")
        self.sortAscendRadio = QtWidgets.QRadioButton(self.sortBox)
        self.sortAscendRadio.setGeometry(QtCore.QRect(70, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortAscendRadio.setFont(font)
        self.sortAscendRadio.setObjectName("sortAscendRadio")
        self.sortDescendRadio = QtWidgets.QRadioButton(self.sortBox)
        self.sortDescendRadio.setGeometry(QtCore.QRect(70, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sortDescendRadio.setFont(font)
        self.sortDescendRadio.setObjectName("sortDescendRadio")
        self.sortLayout.addWidget(self.sortBox)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.refreshButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.refreshButton.setFont(font)
        self.refreshButton.setCheckable(False)
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout_5.addWidget(self.refreshButton)
        self.zoomOutButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.zoomOutButton.setFont(font)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.verticalLayout_5.addWidget(self.zoomOutButton)
        self.sortLayout.addLayout(self.verticalLayout_5)
        self.FullLayout.addLayout(self.sortLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dateLayout = QtWidgets.QVBoxLayout()
        self.dateLayout.setObjectName("dateLayout")
        self.dateTitleLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.dateTitleLabel.setFont(font)
        self.dateTitleLabel.setObjectName("dateTitleLabel")
        self.dateLayout.addWidget(self.dateTitleLabel)
        self.dateLabel = QtWidgets.QLabel(Dialog)
        self.dateLabel.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.dateLabel.setFont(font)
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.dateLayout.addWidget(self.dateLabel)
        self.horizontalLayout_3.addLayout(self.dateLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.categoryLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")
        self.verticalLayout.addWidget(self.categoryLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.availCategoryBox = QtWidgets.QComboBox(Dialog)
        self.availCategoryBox.setMinimumSize(QtCore.QSize(340, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.availCategoryBox.setFont(font)
        self.availCategoryBox.setObjectName("availCategoryBox")
        self.horizontalLayout_4.addWidget(self.availCategoryBox)
        self.categoryEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.categoryEdit.setFont(font)
        self.categoryEdit.setObjectName("categoryEdit")
        self.horizontalLayout_4.addWidget(self.categoryEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.submitButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_3.addWidget(self.submitButton)
        self.FullLayout.addLayout(self.horizontalLayout_3)
        self.displayArea = QtWidgets.QScrollArea(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.displayArea.setFont(font)
        self.displayArea.setWidgetResizable(True)
        self.displayArea.setObjectName("displayArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 548))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imgLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imgLabel.setGeometry(QtCore.QRect(0, 0, 1001, 550))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.imgLabel.setFont(font)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.displayArea.setWidget(self.scrollAreaWidgetContents)
        self.FullLayout.addWidget(self.displayArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.inputPathLabel.setText(_translate("Dialog", "Path of folder to sort"))
        self.browseButton.setText(_translate("Dialog", "Browse"))
        self.numImageLabel.setText(_translate("Dialog", "# of images in each row"))
        self.borderLabel.setText(_translate("Dialog", "Border width"))
        self.sortByBox.setTitle(_translate("Dialog", "Sort by:"))
        self.sortFileNameRadio.setText(_translate("Dialog", "Name"))
        self.sortNoRadio.setText(_translate("Dialog", "None"))
        self.sortModDateRadio.setText(_translate("Dialog", "Modification Date"))
        self.sortFileSizeRadio.setText(_translate("Dialog", "File Size"))
        self.sortCreateDateRadio.setText(_translate("Dialog", "Creation Date"))
        self.sortBox.setTitle(_translate("Dialog", "Sort:"))
        self.sortAscendRadio.setText(_translate("Dialog", "Ascending"))
        self.sortDescendRadio.setText(_translate("Dialog", "Descending"))
        self.refreshButton.setText(_translate("Dialog", "Refresh"))
        self.zoomOutButton.setText(_translate("Dialog", "Zoom out"))
        self.dateTitleLabel.setText(_translate("Dialog", "Date"))
        self.categoryLabel.setText(_translate("Dialog", "Select image category (Folder name to insert into)\n"
"from dropdown or insert new category"))
        self.submitButton.setText(_translate("Dialog", "Submit"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Create GUI object
    window = gui.GUI()
    # Set the title
    window.setWindowTitle("View Images")
    # Set the position and size of the dialog box (x-pos, y-pos, width, height)
    # window.setGeometry(0, 100, 400, 200)
    window.show()
    # Execute the application
    sys.exit(app.exec_())
