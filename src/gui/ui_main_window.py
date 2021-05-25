# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(584, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.browse_layout = QVBoxLayout()
        self.browse_layout.setSpacing(4)
        self.browse_layout.setObjectName(u"browse_layout")
        self.browse_lb_heading = QLabel(self.centralwidget)
        self.browse_lb_heading.setObjectName(u"browse_lb_heading")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.browse_lb_heading.setFont(font)

        self.browse_layout.addWidget(self.browse_lb_heading)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.browse_le_path = QLineEdit(self.centralwidget)
        self.browse_le_path.setObjectName(u"browse_le_path")
        self.browse_le_path.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.browse_le_path)


        self.browse_layout.addLayout(self.horizontalLayout_3)

        self.browse_btn_browse = QPushButton(self.centralwidget)
        self.browse_btn_browse.setObjectName(u"browse_btn_browse")
        icon = QIcon()
        iconThemeName = u"list-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.browse_btn_browse.setIcon(icon)

        self.browse_layout.addWidget(self.browse_btn_browse)

        self.browse_tbv_info = QTableWidget(self.centralwidget)
        if (self.browse_tbv_info.columnCount() < 6):
            self.browse_tbv_info.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.browse_tbv_info.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.browse_tbv_info.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.browse_tbv_info.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.browse_tbv_info.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.browse_tbv_info.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.browse_tbv_info.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.browse_tbv_info.setObjectName(u"browse_tbv_info")
        self.browse_tbv_info.setSelectionMode(QAbstractItemView.SingleSelection)
        self.browse_tbv_info.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.browse_tbv_info.setColumnCount(6)
        self.browse_tbv_info.horizontalHeader().setCascadingSectionResizes(False)
        self.browse_tbv_info.horizontalHeader().setMinimumSectionSize(25)
        self.browse_tbv_info.horizontalHeader().setDefaultSectionSize(100)
        self.browse_tbv_info.horizontalHeader().setProperty("showSortIndicator", True)
        self.browse_tbv_info.horizontalHeader().setStretchLastSection(False)

        self.browse_layout.addWidget(self.browse_tbv_info)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.browse_btn_start = QPushButton(self.centralwidget)
        self.browse_btn_start.setObjectName(u"browse_btn_start")
        self.browse_btn_start.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.browse_btn_start)

        self.browse_btn_open = QPushButton(self.centralwidget)
        self.browse_btn_open.setObjectName(u"browse_btn_open")
        self.browse_btn_open.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.browse_btn_open)


        self.browse_layout.addLayout(self.horizontalLayout_8)


        self.gridLayout_2.addLayout(self.browse_layout, 4, 0, 1, 1)

        self.break_1 = QFrame(self.centralwidget)
        self.break_1.setObjectName(u"break_1")
        self.break_1.setFrameShape(QFrame.HLine)
        self.break_1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.break_1, 3, 0, 1, 1)

        self.image_layout = QVBoxLayout()
        self.image_layout.setSpacing(4)
        self.image_layout.setObjectName(u"image_layout")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.image_layout.addWidget(self.label_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.image_title = QLineEdit(self.centralwidget)
        self.image_title.setObjectName(u"image_title")

        self.horizontalLayout_5.addWidget(self.image_title)


        self.image_layout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_9.addWidget(self.label_7)

        self.image_subject = QLineEdit(self.centralwidget)
        self.image_subject.setObjectName(u"image_subject")

        self.horizontalLayout_9.addWidget(self.image_subject)


        self.image_layout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))

        self.horizontalLayout.addWidget(self.label)

        self.image_comments = QLineEdit(self.centralwidget)
        self.image_comments.setObjectName(u"image_comments")

        self.horizontalLayout.addWidget(self.image_comments)


        self.image_layout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.image_author = QLineEdit(self.centralwidget)
        self.image_author.setObjectName(u"image_author")

        self.horizontalLayout_2.addWidget(self.image_author)


        self.image_layout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.image_layout, 2, 0, 1, 1)

        self.config_layout = QVBoxLayout()
        self.config_layout.setSpacing(4)
        self.config_layout.setObjectName(u"config_layout")
        self.config_lb_heading = QLabel(self.centralwidget)
        self.config_lb_heading.setObjectName(u"config_lb_heading")
        self.config_lb_heading.setFont(font)

        self.config_layout.addWidget(self.config_lb_heading)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_10.addWidget(self.label_8)

        self.config_le_output = QLineEdit(self.centralwidget)
        self.config_le_output.setObjectName(u"config_le_output")

        self.horizontalLayout_10.addWidget(self.config_le_output)


        self.config_layout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.config_le_max_size_kb = QLineEdit(self.centralwidget)
        self.config_le_max_size_kb.setObjectName(u"config_le_max_size_kb")

        self.horizontalLayout_7.addWidget(self.config_le_max_size_kb)


        self.config_layout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.config_le_standard_width = QLineEdit(self.centralwidget)
        self.config_le_standard_width.setObjectName(u"config_le_standard_width")

        self.horizontalLayout_6.addWidget(self.config_le_standard_width)


        self.config_layout.addLayout(self.horizontalLayout_6)


        self.gridLayout_2.addLayout(self.config_layout, 0, 0, 1, 1)

        self.break_2 = QFrame(self.centralwidget)
        self.break_2.setObjectName(u"break_2")
        self.break_2.setFrameShape(QFrame.HLine)
        self.break_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.break_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browse_lb_heading.setText(QCoreApplication.translate("MainWindow", u"3. Ch\u1ecdn th\u01b0 m\u1ee5c ch\u1ee9a \u1ea3nh", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01b0\u1eddng d\u1eabn th\u01b0 m\u1ee5c", None))
        self.browse_le_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ch\u01b0a c\u00f3 th\u01b0 m\u1ee5c \u0111\u01b0\u1ee3c ch\u1ecdn", None))
        self.browse_btn_browse.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn th\u01b0 m\u1ee5c", None))
        ___qtablewidgetitem = self.browse_tbv_info.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem1 = self.browse_tbv_info.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecbnh d\u1ea1ng", None));
        ___qtablewidgetitem2 = self.browse_tbv_info.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"KT \u0111\u1ea7u", None));
        ___qtablewidgetitem3 = self.browse_tbv_info.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"KT sau", None));
        ___qtablewidgetitem4 = self.browse_tbv_info.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"KT \u0111\u1ea7u (KB)", None));
        ___qtablewidgetitem5 = self.browse_tbv_info.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"KT sau (KB)", None));
        self.browse_btn_start.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u ch\u1ea1y", None))
        self.browse_btn_open.setText(QCoreApplication.translate("MainWindow", u"M\u1edf th\u01b0 m\u1ee5c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2. Th\u00f4ng tin \u1ea3nh", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.image_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0110\u1ec3 tr\u1ed1ng", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.image_subject.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0110\u1ec3 tr\u1ed1ng", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Comments", None))
        self.image_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0110\u1ec3 tr\u1ed1ng", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Authors & Copyright", None))
        self.image_author.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0110\u1ec3 tr\u1ed1ng", None))
        self.config_lb_heading.setText(QCoreApplication.translate("MainWindow", u"1. C\u1ea5u h\u00ecnh", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Th\u01b0 m\u1ee5c l\u01b0u", None))
        self.config_le_output.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u1ed1i \u0111a (KB)", None))
        self.config_le_max_size_kb.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.config_le_max_size_kb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u r\u1ed9ng chu\u1ea9n", None))
        self.config_le_standard_width.setText(QCoreApplication.translate("MainWindow", u"1200", None))
        self.config_le_standard_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1200", None))
    # retranslateUi

