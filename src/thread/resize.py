from os import stat
from PySide2.QtCore import QRunnable, Slot
from PySide2.QtWidgets import QStatusBar, QTableWidget
from image.resizer import ImageResizer
from PySide2.QtCore import Qt
from PySide2 import QtWidgets
import logging

from utils.file_utils import FileUtils

class ResizeThread(QRunnable):
  def set_status_bar(self, status_bar: QStatusBar):
    self.status_bar = status_bar

  def set_table_view(self, table_view: QTableWidget):
    self.table_view = table_view

  def set_prefix(self, prefix):
    self.prefix = prefix

  def set_postfix(self, postfix):
    self.postfix = postfix

  def set_max_size_kb(self, max_size_kb):
    self.max_size_kb = max_size_kb

  def set_standard_width(self, standard_width):
    self.standard_width = standard_width

  @Slot()
  def run(self):
    if (self.prefix is None):
      self.prefix = ""

    if (self.postfix is None):
      self.postfix = ""

    # selection_model = self.table_view.selectionModel()
    # selected_row = selection_model.selectedRows()[0].row()
    selected_row = 0
    row_count = self.table_view.rowCount()

    logging.info("Start from row {} to {}".format(selected_row, row_count))

    for i in range(selected_row, row_count):
      path = self.table_view.item(i, 0).text()
      resizer = ImageResizer(path, self.max_size_kb, self.prefix, self.postfix)
      new_path = resizer.resize_with_width(self.standard_width)
      file_size = FileUtils.get_file_size(new_path)
      # self.table_view.selectRow(i)

      file_size_item = QtWidgets.QTableWidgetItem("{}KB".format(int(file_size / 1024)))
      file_size_item.setTextAlignment(Qt.AlignRight | Qt.AlignHCenter)
      self.table_view.setItem(i, 5, file_size_item)

      self.status_bar.showMessage("Lưu {}".format(new_path))

    self.status_bar.showMessage("Đã lưu {} ảnh, chọn [Mở thư mục] để kiểm tra".format(row_count))
