from PySide2 import QtWidgets
from gui.ui_main_window import Ui_MainWindow
from PySide2.QtWidgets  import QFileDialog, QMainWindow, QDialog, QHeaderView
from PySide2.QtCore import Qt, QThreadPool
from PySide2.QtGui import QIntValidator
import logging
from thread.resize import ResizeThread
from config import Config
from utils.file_utils import FileUtils
from utils.img_utils import ImgUtils

class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.threadpool = QThreadPool()
    self.setupUi(self)
    self.setWindowTitle("Wiopt - Web images optimizer")
    self.setMinimumWidth(800)
    self.setMinimumHeight(600)
    self.connect()
    self.load_config()

  def connect(self):
    logging.debug('Connect browse_btn_browse to openbox')
    self.browse_btn_browse.clicked.connect(self.openbox)

    logging.debug("Set browse_tbv_info header id=0 to stretch mode")
    self.browse_tbv_info.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    logging.debug("Connect browse_btn_start to start_resizing")
    self.browse_btn_start.clicked.connect(self.start_resizing)

    logging.debug("Connect browse_btn_open to open_folder")
    self.browse_btn_open.clicked.connect(self.open_folder)

    logging.debug("Set int validator for config_le_max_size_kb")
    self.config_le_max_size_kb.setValidator(QIntValidator(10, 8192, self))

    logging.debug("Set int validator for config_le_standard_width")
    self.config_le_standard_width.setValidator(QIntValidator(800, 9999, self))

  def load_config(self):
    conf = Config.read()
    logging.debug('Current config {}'.format(conf))
    self.browse_le_path.setText(conf['last_open_path'])
    self.config_le_standard_width.setText(conf['standard_width'])
    self.config_le_max_size_kb.setText(conf['max_size_kb'])
    self.config_le_prefix.setText(conf['last_prefix'])
    self.config_le_postfix.setText(conf['last_postfix'])

  def openbox(self):
    dialog = QFileDialog(self)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    dialog.setFileMode(QFileDialog.DirectoryOnly)

    if dialog.exec_() == QDialog.Accepted:
        path = dialog.selectedFiles()[0]
        logging.info("Open folder {}".format(path))
        self.update_browse_section(path)
        Config.write('last_open_path', path)
    else:
        return ''

  def open_folder(self):
    path = self.browse_le_path.text()
    FileUtils.show_file(path)

  def update_browse_section(self, path: str):
    logging.info("Set browse_le_path text to {}".format(path))
    self.browse_le_path.setText(path)
    self.browse_tbv_info.setRowCount(0)
    prefix = self.config_le_prefix.text()
    new_width = int(self.config_le_standard_width.text())

    self.statusbar.showMessage("Đã chọn đường dẫn {}".format(path))

    files_stat = FileUtils.list_images_with_stats(path, prefix)

    for file_stat in files_stat:
      logging.debug("Add data to table browse_tbv_info {}".format(file_stat))
      rowPosition = self.browse_tbv_info.rowCount()
      (w, h) = ImgUtils.get_image_size(file_stat['path'])
      new_height = int(new_width / (w / h))

      file_size_item = QtWidgets.QTableWidgetItem("{}KB".format(file_stat['sizeKB']))
      file_size_item.setTextAlignment(Qt.AlignRight | Qt.AlignHCenter)

      self.browse_tbv_info.insertRow(rowPosition)
      self.browse_tbv_info.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(file_stat['path']))
      self.browse_tbv_info.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(file_stat['format']))
      self.browse_tbv_info.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem("{}x{}".format(w, h)))
      self.browse_tbv_info.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem("{}x{}".format(new_width, new_height)))
      self.browse_tbv_info.setItem(rowPosition, 4, file_size_item)

    if (self.browse_tbv_info.rowCount() > 0):
      logging.debug("Select first row of table")
      self.browse_tbv_info.selectRow(0)
    
    self.statusbar.showMessage("Mở {} ảnh".format(self.browse_tbv_info.rowCount()))

  def start_resizing(self):
    prefix = self.config_le_prefix.text()
    postfix = self.config_le_postfix.text()
    width = (int)(self.config_le_standard_width.text())
    max_kb = (int)(self.config_le_max_size_kb.text())

    Config.write('last_prefix', prefix)
    Config.write('last_postfix', postfix)
    Config.write('max_size_kb', max_kb)
    Config.write("standard_width", width)

    resize_thread = ResizeThread()
    resize_thread.set_status_bar(self.statusbar)
    resize_thread.set_table_view(self.browse_tbv_info)
    resize_thread.set_prefix(prefix)
    resize_thread.set_postfix(postfix)
    resize_thread.set_standard_width(width)
    resize_thread.set_max_size_kb(max_kb)

    self.threadpool.start(resize_thread)

