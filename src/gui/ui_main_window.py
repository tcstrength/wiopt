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
        MainWindow.resize(595, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.config_layout = QVBoxLayout()
        self.config_layout.setObjectName(u"config_layout")
        self.config_lb_heading = QLabel(self.centralwidget)
        self.config_lb_heading.setObjectName(u"config_lb_heading")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.config_lb_heading.setFont(font)

        self.config_layout.addWidget(self.config_lb_heading)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.config_le_prefix = QLineEdit(self.centralwidget)
        self.config_le_prefix.setObjectName(u"config_le_prefix")

        self.horizontalLayout_4.addWidget(self.config_le_prefix)


        self.config_layout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))

        self.horizontalLayout.addWidget(self.label)

        self.config_le_postfix = QLineEdit(self.centralwidget)
        self.config_le_postfix.setObjectName(u"config_le_postfix")

        self.horizontalLayout.addWidget(self.config_le_postfix)


        self.config_layout.addLayout(self.horizontalLayout)

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


        self.verticalLayout.addLayout(self.config_layout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.browse_layout = QVBoxLayout()
        self.browse_layout.setObjectName(u"browse_layout")
        self.browse_lb_heading = QLabel(self.centralwidget)
        self.browse_lb_heading.setObjectName(u"browse_lb_heading")
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


        self.verticalLayout.addLayout(self.browse_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.config_lb_heading.setText(QCoreApplication.translate("MainWindow", u"1. C\u1ea5u h\u00ecnh", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ch\u00e8n ph\u00eda tr\u01b0\u1edbc t\u00ean", None))
        self.config_le_prefix.setText(QCoreApplication.translate("MainWindow", u"resized_", None))
        self.config_le_prefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng ch\u00e8n g\u00ec", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ch\u00e8n ph\u00eda sau t\u00ean", None))
        self.config_le_postfix.setText("")
        self.config_le_postfix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng ch\u00e8n g\u00ec", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u1ed1i \u0111a (KB)", None))
        self.config_le_max_size_kb.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.config_le_max_size_kb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u r\u1ed9ng chu\u1ea9n", None))
        self.config_le_standard_width.setText(QCoreApplication.translate("MainWindow", u"1200", None))
        self.config_le_standard_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1200", None))
        self.browse_lb_heading.setText(QCoreApplication.translate("MainWindow", u"2. Ch\u1ecdn th\u01b0 m\u1ee5c ch\u1ee9a \u1ea3nh", None))
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
    # retranslateUi

