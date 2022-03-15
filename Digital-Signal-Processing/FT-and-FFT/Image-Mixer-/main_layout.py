# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Mixer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1294, 912)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.image_1_container = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.image_1_container.setFont(font)
        self.image_1_container.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.image_1_container.setObjectName("image_1_container")
        self.gridLayout = QtWidgets.QGridLayout(self.image_1_container)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.image_1_pick = QtWidgets.QComboBox(self.image_1_container)
        self.image_1_pick.setEnabled(False)
        self.image_1_pick.setObjectName("image_1_pick")
        self.image_1_pick.addItem("")
        self.image_1_pick.setItemText(0, "")
        self.image_1_pick.addItem("")
        self.image_1_pick.addItem("")
        self.image_1_pick.addItem("")
        self.image_1_pick.addItem("")
        self.gridLayout.addWidget(self.image_1_pick, 0, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.image_1_original = QtWidgets.QLabel(self.image_1_container)
        self.image_1_original.setMinimumSize(QtCore.QSize(300, 300))
        self.image_1_original.setText("")
        self.image_1_original.setPixmap(QtGui.QPixmap(".\\placeholder.png"))
        self.image_1_original.setObjectName("image_1_original")
        self.horizontalLayout_8.addWidget(self.image_1_original)
        self.image_1_after_filter = QtWidgets.QLabel(self.image_1_container)
        self.image_1_after_filter.setMinimumSize(QtCore.QSize(300, 300))
        self.image_1_after_filter.setText("")
        self.image_1_after_filter.setPixmap(QtGui.QPixmap(".\\placeholder.png"))
        self.image_1_after_filter.setObjectName("image_1_after_filter")
        self.horizontalLayout_8.addWidget(self.image_1_after_filter)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.image_1_container, 0, 0, 1, 1)
        self.mixer_container = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mixer_container.setFont(font)
        self.mixer_container.setObjectName("mixer_container")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mixer_container)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mixer_output_to_label = QtWidgets.QLabel(self.mixer_container)
        self.mixer_output_to_label.setObjectName("mixer_output_to_label")
        self.horizontalLayout_4.addWidget(self.mixer_output_to_label)
        self.output_select = QtWidgets.QComboBox(self.mixer_container)
        self.output_select.setEnabled(False)
        self.output_select.setObjectName("output_select")
        self.output_select.addItem("")
        self.output_select.setItemText(0, "")
        self.output_select.addItem("")
        self.output_select.addItem("")
        self.horizontalLayout_4.addWidget(self.output_select)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.component_1_label = QtWidgets.QLabel(self.mixer_container)
        self.component_1_label.setObjectName("component_1_label")
        self.horizontalLayout_3.addWidget(self.component_1_label)
        self.component_1_select = QtWidgets.QComboBox(self.mixer_container)
        self.component_1_select.setEnabled(False)
        self.component_1_select.setMinimumSize(QtCore.QSize(116, 30))
        self.component_1_select.setObjectName("component_1_select")
        self.component_1_select.addItem("")
        self.component_1_select.setItemText(0, "")
        self.horizontalLayout_3.addWidget(self.component_1_select)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.component_1_percentage = QtWidgets.QProgressBar(self.mixer_container)
        self.component_1_percentage.setEnabled(False)
        self.component_1_percentage.setProperty("value", 0)
        self.component_1_percentage.setObjectName("component_1_percentage")
        self.verticalLayout.addWidget(self.component_1_percentage)
        self.component_1_slider = QtWidgets.QSlider(self.mixer_container)
        self.component_1_slider.setEnabled(False)
        self.component_1_slider.setMaximum(100)
        self.component_1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component_1_slider.setObjectName("component_1_slider")
        self.verticalLayout.addWidget(self.component_1_slider)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.component_1_type = QtWidgets.QComboBox(self.mixer_container)
        self.component_1_type.setEnabled(False)
        self.component_1_type.setObjectName("component_1_type")
        self.component_1_type.addItem("")
        self.component_1_type.setItemText(0, "")
        self.component_1_type.addItem("")
        self.component_1_type.addItem("")
        self.component_1_type.addItem("")
        self.component_1_type.addItem("")
        self.component_1_type.addItem("")
        self.component_1_type.addItem("")
        self.verticalLayout_4.addWidget(self.component_1_type)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.component_2_label = QtWidgets.QLabel(self.mixer_container)
        self.component_2_label.setObjectName("component_2_label")
        self.horizontalLayout_5.addWidget(self.component_2_label)
        self.component_2_select = QtWidgets.QComboBox(self.mixer_container)
        self.component_2_select.setEnabled(False)
        self.component_2_select.setMinimumSize(QtCore.QSize(116, 30))
        self.component_2_select.setObjectName("component_2_select")
        self.component_2_select.addItem("")
        self.component_2_select.setItemText(0, "")
        self.horizontalLayout_5.addWidget(self.component_2_select)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.component_2_percentage = QtWidgets.QProgressBar(self.mixer_container)
        self.component_2_percentage.setEnabled(False)
        self.component_2_percentage.setProperty("value", 0)
        self.component_2_percentage.setObjectName("component_2_percentage")
        self.verticalLayout_3.addWidget(self.component_2_percentage)
        self.component_2_slider = QtWidgets.QSlider(self.mixer_container)
        self.component_2_slider.setEnabled(False)
        self.component_2_slider.setMaximum(100)
        self.component_2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component_2_slider.setObjectName("component_2_slider")
        self.verticalLayout_3.addWidget(self.component_2_slider)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.component_2_type = QtWidgets.QComboBox(self.mixer_container)
        self.component_2_type.setEnabled(False)
        self.component_2_type.setObjectName("component_2_type")
        self.component_2_type.addItem("")
        self.component_2_type.setItemText(0, "")
        self.component_2_type.addItem("")
        self.component_2_type.addItem("")
        self.component_2_type.addItem("")
        self.component_2_type.addItem("")
        self.component_2_type.addItem("")
        self.component_2_type.addItem("")
        self.verticalLayout_2.addWidget(self.component_2_type)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout_4.addWidget(self.mixer_container, 0, 1, 1, 1)
        self.image_1_container_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.image_1_container_2.setFont(font)
        self.image_1_container_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.image_1_container_2.setObjectName("image_1_container_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.image_1_container_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.image_2_pick = QtWidgets.QComboBox(self.image_1_container_2)
        self.image_2_pick.setEnabled(False)
        self.image_2_pick.setObjectName("image_2_pick")
        self.image_2_pick.addItem("")
        self.image_2_pick.setItemText(0, "")
        self.image_2_pick.addItem("")
        self.image_2_pick.addItem("")
        self.image_2_pick.addItem("")
        self.image_2_pick.addItem("")
        self.gridLayout_2.addWidget(self.image_2_pick, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.image_2_original = QtWidgets.QLabel(self.image_1_container_2)
        self.image_2_original.setMinimumSize(QtCore.QSize(300, 300))
        self.image_2_original.setText("")
        self.image_2_original.setPixmap(QtGui.QPixmap(".\\placeholder.png"))
        self.image_2_original.setObjectName("image_2_original")
        self.horizontalLayout_9.addWidget(self.image_2_original)
        self.image_2_after_filter = QtWidgets.QLabel(self.image_1_container_2)
        self.image_2_after_filter.setMinimumSize(QtCore.QSize(300, 300))
        self.image_2_after_filter.setText("")
        self.image_2_after_filter.setPixmap(QtGui.QPixmap(".\\placeholder.png"))
        self.image_2_after_filter.setObjectName("image_2_after_filter")
        self.horizontalLayout_9.addWidget(self.image_2_after_filter)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.image_1_container_2, 1, 0, 1, 1)
        self.output_container = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_container.setFont(font)
        self.output_container.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_container.setObjectName("output_container")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.output_container)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.output_1_label = QtWidgets.QLabel(self.output_container)
        self.output_1_label.setObjectName("output_1_label")
        self.horizontalLayout_7.addWidget(self.output_1_label)
        self.output_2_label = QtWidgets.QLabel(self.output_container)
        self.output_2_label.setObjectName("output_2_label")
        self.horizontalLayout_7.addWidget(self.output_2_label)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.output_1 = QtWidgets.QLabel(self.output_container)
        self.output_1.setMinimumSize(QtCore.QSize(300, 300))
        self.output_1.setText("")
        self.output_1.setPixmap(QtGui.QPixmap(".\\placeholder.png"))
        self.output_1.setObjectName("output_1")
        self.horizontalLayout_10.addWidget(self.output_1)
        self.output_2 = QtWidgets.QLabel(self.output_container)
        self.output_2.setMinimumSize(QtCore.QSize(300, 300))
        self.output_2.setText("")
        self.output_2.setPixmap(QtGui.QPixmap(".\\placeholder.png"))
        self.output_2.setObjectName("output_2")
        self.horizontalLayout_10.addWidget(self.output_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.output_container, 1, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1294, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open_image_1 = QtWidgets.QAction(MainWindow)
        self.action_open_image_1.setObjectName("action_open_image_1")
        self.action_open_image_2 = QtWidgets.QAction(MainWindow)
        self.action_open_image_2.setObjectName("action_open_image_2")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menuOpen.addAction(self.action_open_image_1)
        self.menuOpen.addAction(self.action_open_image_2)
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.action_exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.component_1_slider.valueChanged['int'].connect(self.component_1_percentage.setValue)
        self.component_2_slider.valueChanged['int'].connect(self.component_2_percentage.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_1_container.setTitle(_translate("MainWindow", "Image 1"))
        self.image_1_pick.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.image_1_pick.setItemText(2, _translate("MainWindow", "Phase"))
        self.image_1_pick.setItemText(3, _translate("MainWindow", "Real"))
        self.image_1_pick.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.mixer_container.setTitle(_translate("MainWindow", "Mixer"))
        self.mixer_output_to_label.setText(_translate("MainWindow", "Mixer Output to:"))
        self.output_select.setItemText(1, _translate("MainWindow", "Output 1"))
        self.output_select.setItemText(2, _translate("MainWindow", "Output 2"))
        self.component_1_label.setText(_translate("MainWindow", "Component 1   "))
        self.component_1_type.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.component_1_type.setItemText(2, _translate("MainWindow", "Phase"))
        self.component_1_type.setItemText(3, _translate("MainWindow", "Real"))
        self.component_1_type.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.component_1_type.setItemText(5, _translate("MainWindow", "Uniform Magnitude"))
        self.component_1_type.setItemText(6, _translate("MainWindow", "Uniform Phase"))
        self.component_2_label.setText(_translate("MainWindow", "Component 2   "))
        self.component_2_type.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.component_2_type.setItemText(2, _translate("MainWindow", "Phase"))
        self.component_2_type.setItemText(3, _translate("MainWindow", "Real"))
        self.component_2_type.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.component_2_type.setItemText(5, _translate("MainWindow", "Uniform Magnitude"))
        self.component_2_type.setItemText(6, _translate("MainWindow", "Uniform Phase"))
        self.image_1_container_2.setTitle(_translate("MainWindow", "Image 2"))
        self.image_2_pick.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.image_2_pick.setItemText(2, _translate("MainWindow", "Phase"))
        self.image_2_pick.setItemText(3, _translate("MainWindow", "Real"))
        self.image_2_pick.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.output_container.setTitle(_translate("MainWindow", "Output"))
        self.output_1_label.setText(_translate("MainWindow", "Output 1"))
        self.output_2_label.setText(_translate("MainWindow", "Output 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open_image_1.setText(_translate("MainWindow", "Image 1"))
        self.action_open_image_1.setShortcut(_translate("MainWindow", "1"))
        self.action_open_image_2.setText(_translate("MainWindow", "Image 2"))
        self.action_open_image_2.setShortcut(_translate("MainWindow", "2"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
